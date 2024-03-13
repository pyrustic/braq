import unittest
import pathlib
import tempfile
from textwrap import dedent
from braq.document import Document
from braq.section import Section
from paradict import box
from paradict.errors import Error as ParadictError


INIT_TEXT = """\
line 1
line 2

[section 1]
name = "alex"
pi = 3.14

[section 2]
id = 42

[section 3]
website = 404"""


SCHEMA = {"section 1":
              {"name": "str",
               "pi": "float"},
          "section 2":
              {"id": "int"},
          "section 3":
              {"website": "str"}}


SCHEMA_TEXT = """\
[section 1]
name = "str"
pi = "float"

[section 2]
id = "int"

[section 3]
website = "str"\
"""


class TestEmptyDocument(unittest.TestCase):

    def setUp(self):
        self._document = Document()

    def test_get_method(self):
        r = self._document.get("section 1")
        self.assertIsNone(r)

    def test_get_lines_method(self):
        r = self._document.get_lines("section 1")
        self.assertIsNone(r)

    def test_set_method(self):
        with self.subTest():
            section_1 = ("section 1", ["line 1", "line 2"])
            self._document.set(*section_1)
            r = self._document.get("section 1")
            expected = "line 1\nline 2"
            self.assertEqual(expected, r)
        with self.subTest():
            section_2 = ("section 2", "line 3\nline 4")
            self._document.set(*section_2)
            r = self._document.get("section 2")
            expected = "line 3\nline 4"
            self.assertEqual(expected, r)
        with self.subTest():
            section_3 = Section("section 3", "line 5\nline 6")
            self._document.set(*section_3)
            r = self._document.get("section 3")
            expected = "line 5\nline 6"
            self.assertEqual(expected, r)

    def test_build_method(self):
        data = {"name": "alex", "pi": 3.14}
        self._document.embed("section 1", data)
        self._document.set("section 2", "line 1\nline 2")
        with self.subTest():
            r = self._document.build("section 1")
            self.assertEqual(data, r)
        with self.assertRaises(ParadictError):
            self._document.build("section 2")

    def test_build_config_method(self):
        data = {"name": "alex", "pi": 3.14}
        self._document.embed("section 1", data)
        self._document.set("section 2", "line 1\nline 2")
        with self.subTest():
            r = self._document.build_config("section 1")
            expected = {"section 1": data}
            self.assertEqual(expected, r)
        with self.subTest():
            err_cache = list()
            on_error = lambda header, err: err_cache.append((header, err))
            r = self._document.build_config("section 1", "section 2",
                                            on_error=on_error)
            expected = {"section 1": data, "section 2": None}
            self.assertEqual(expected, r)
            self.assertEqual(1, len(err_cache))
        with self.subTest():
            r = self._document.build_config()
            expected = {"section 1": data, "section 2": None}
            self.assertEqual(expected, r)

    def test_embed_method(self):
        data = {"name": "alex", "pi": 3.14}
        self._document.embed("section 1", data)
        r = self._document.get("section 1")
        expected = 'name = "alex"\npi = 3.14'
        self.assertEqual(expected, r)

    def test_list_headers_method(self):
        r = self._document.list_headers()
        expected = tuple()
        self.assertEqual(expected, r)

    def test_render_method(self):
        r = self._document.render()
        expected = str()
        self.assertEqual(expected, r)

    def test_remove_method(self):
        # 1
        with self.subTest("Test 'remove' method without argument"):
            try:
                self._document.remove()
            except Exception as e:
                self.assertTrue(False)
        # 2
        with self.subTest("Test 'remove' method with argument"):
            try:
                self._document.remove("header")
            except Exception as e:
                self.assertTrue(False)

    def test_clear_method(self):
        try:
            self._document.clear()
        except Exception as e:
            self.assertTrue(False)


class TestDocument(unittest.TestCase):

    def setUp(self):
        self._document = Document(INIT_TEXT)

    def test_get_method(self):
        r = self._document.get("section 1")
        expected = 'name = "alex"\npi = 3.14'
        self.assertEqual(expected, r)

    def test_get_lines_method(self):
        r = self._document.get_lines("section 1")
        expected = ['name = "alex"', "pi = 3.14"]
        self.assertEqual(expected, r)

    def test_set_method(self):
        data = ['name = "alex"', 'pi = 0']
        self._document.set("section 1", data)
        r = self._document.get("section 1")
        expected = 'name = "alex"\npi = 0'
        self.assertEqual(expected, r)

    def test_build_method(self):
        with self.subTest():
            r = self._document.build("section 1")
            expected = {"name": "alex", "pi": 3.14}
            self.assertEqual(expected, r)
        with self.assertRaises(ParadictError):
            self._document.build("")

    def test_build_config_method(self):
        data = {"name": "alex", "pi": 3.14}
        with self.subTest():
            r = self._document.build_config("section 1")
            expected = {"section 1": data}
            self.assertEqual(expected, r)
        with self.subTest():
            r = self._document.build_config("section 1", "section 2")
            expected = {"section 1": data, "section 2": {"id": 42}}
            self.assertEqual(expected, r)
        with self.subTest():
            err_cache = list()
            on_error = lambda header, err: err_cache.append((header, err))
            r = self._document.build_config(on_error=on_error)
            expected = {"": None, "section 1": data, "section 2": {"id": 42},
                        "section 3": {"website": 404}}
            self.assertEqual(expected, r)
            self.assertEqual(1, len(err_cache))

    def test_embed_method(self):
        data = {"name": "alex", "pi": 0}
        self._document.embed("section 1", data)
        r = self._document.get("section 1")
        expected = 'name = "alex"\npi = 0'
        self.assertEqual(expected, r)

    def test_list_headers_method(self):
        r = self._document.list_headers()
        expected = ("", "section 1", "section 2", "section 3")
        self.assertEqual(expected, r)

    def test_render_method(self):
        # 1
        with self.subTest("Render the entire doc"):
            r = self._document.render()
            expected = INIT_TEXT
            self.assertEqual(expected, r)
        # 2
        with self.subTest("Render the unnamed section"):
            r = self._document.render("")
            expected = "line 1\nline 2"
            self.assertEqual(expected, r)
        # 3
        with self.subTest("Render section 1"):
            r = self._document.render("section 1")
            expected = """\
            [section 1]
            name = "alex"
            pi = 3.14"""
            self.assertEqual(dedent(expected), r)

    def test_remove_method(self):
        # 1
        with self.subTest("Test 'remove' method without argument"):
            self._document.remove()
            r = self._document.list_headers()
            expected = ("", "section 1", "section 2", "section 3")
            self.assertEqual(expected, r)
        # 2
        with self.subTest("Test 'remove' method with argument"):
            self._document.remove("section 1")
            r = self._document.list_headers()
            expected = ("", "section 2", "section 3")
            self.assertEqual(expected, r)

    def test_clear_method(self):
        self._document.clear()
        r = self._document.list_headers()
        expected = tuple()
        self.assertEqual(expected, r)


class TestDocumentWithComment(unittest.TestCase):

    def setUp(self):
        text = """\
        # this is a comment
        pi = 3.14"""
        self._document = Document(dedent(text))

    def test_build_method_with_default_comments_off(self):
        r = self._document.build("")  # skip_comments=True
        expected = {"pi": 3.14}
        self.assertEqual(expected, r)

    def test_build_method_with_comments_on(self):
        r = self._document.build("", skip_comments=False)
        r = tuple(r.values())
        expected = ("this is a comment", 3.14)
        self.assertEqual(expected, r)

    def test_creating_section_with_comment(self):
        body = {box.CommentID(): box.Comment("This is a comment !"),
                "pi": 3.14}
        self._document.embed("section 1", body)
        r = self._document.build("section 1", skip_comments=False)
        r = tuple(r.values())
        expected = ("This is a comment !", 3.14)
        self.assertEqual(expected, r)


class TestLoadFromFileOperation(unittest.TestCase):

    def setUp(self):
        file = tempfile.NamedTemporaryFile(delete=False)
        file.write(INIT_TEXT.encode("utf-8"))
        file.close()
        self._filename = file.name
        self._document = Document()

    def tearDown(self):
        pathlib.Path(self._filename).unlink()

    def test(self):
        self._document.load_from(self._filename)
        r = self._document.get("section 1")
        expected = 'name = "alex"\npi = 3.14'
        self.assertEqual(expected, r)


class TestSaveToFileOperation(unittest.TestCase):

    def setUp(self):
        file = tempfile.NamedTemporaryFile(delete=False)
        file.close()
        self._filename = file.name
        self._document = Document(INIT_TEXT)

    def tearDown(self):
        pathlib.Path(self._filename).unlink()

    def test(self):
        self._document.save_to(self._filename)
        with open(self._filename, "r", encoding="utf-8") as file:
            r = file.read()
        expected = INIT_TEXT
        self.assertEqual(expected, r)


class TestDocumentWithSchema(unittest.TestCase):

    def setUp(self):
        self._document = Document(INIT_TEXT, schema=SCHEMA)

    def test_schema_property(self):
        r = self._document.schema
        expected = SCHEMA
        self.assertEqual(expected, r)

    def test_validate_method(self):
        # 1
        with self.subTest("Validate the entire doc"):
            r = self._document.validate()
            expected = False
            self.assertEqual(expected, r)
        # 2
        with self.subTest("Validate section 1 and section 2"):
            r = self._document.validate("section 1", "section 2")
            expected = True
            self.assertEqual(expected, r)
        # 3
        with self.subTest("Validate unnamed section and section 3"):
            r = self._document.validate("", "section 3")
            expected = False
            self.assertEqual(expected, r)


class TestDocumentWithEmptySchemaFile(unittest.TestCase):

    def setUp(self):
        file = tempfile.NamedTemporaryFile(delete=False)
        file.close()
        self._filename = file.name
        self._document = Document(INIT_TEXT)
        self._document.load_schema(self._filename)

    def tearDown(self):
        pathlib.Path(self._filename).unlink()

    def test_schema_property(self):
        r = self._document.schema
        expected = dict()
        self.assertEqual(expected, r)

    def test_validate_method(self):
        # 1
        with self.subTest("Validate the entire doc"):
            r = self._document.validate()
            expected = True
            self.assertEqual(expected, r)
        # 2
        with self.subTest("Validate section 1 and section 2"):
            r = self._document.validate("section 1", "section 2")
            expected = True
            self.assertEqual(expected, r)
        # 3
        with self.subTest("Validate unnamed section and section 3"):
            r = self._document.validate("", "section 3")
            expected = True
            self.assertEqual(expected, r)


class TestDocumentWithSchemaFile(unittest.TestCase):

    def setUp(self):
        file = tempfile.NamedTemporaryFile(delete=False)
        file.write(SCHEMA_TEXT.encode("utf-8"))
        file.close()
        self._filename = file.name
        self._document = Document(INIT_TEXT)
        self._document.load_schema(self._filename)

    def tearDown(self):
        pathlib.Path(self._filename).unlink()

    def test_schema_property(self):
        r = self._document.schema
        expected = SCHEMA
        self.assertEqual(expected, r)

    def test_validate_method(self):
        # 1
        with self.subTest("Validate the entire doc"):
            r = self._document.validate()
            expected = False
            self.assertEqual(expected, r)
        # 2
        with self.subTest("Validate section 1 and section 2"):
            r = self._document.validate("section 1", "section 2")
            expected = True
            self.assertEqual(expected, r)
        # 3
        with self.subTest("Validate unnamed section and section 3"):
            r = self._document.validate("", "section 3")
            expected = False
            self.assertEqual(expected, r)


if __name__ == "__main__":
    unittest.main()
