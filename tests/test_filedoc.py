import unittest
import pathlib
import tempfile
from textwrap import dedent
from braq.filedoc import FileDoc
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


def readfile(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


class TestEmptyFileDoc(unittest.TestCase):

    def setUp(self):
        file = tempfile.NamedTemporaryFile(delete=False)
        file.close()
        self._filename = file.name
        self._file_doc = FileDoc(self._filename)

    def tearDown(self):
        pathlib.Path(self._filename).unlink()

    def test_get_method(self):
        r = self._file_doc.get("section 1")
        self.assertIsNone(r)

    def test_get_lines_method(self):
        r = self._file_doc.get_lines("section 1")
        self.assertIsNone(r)

    def test_set_method(self):
        with self.subTest():
            section_1 = ("section 1", ["line 1", "line 2"])
            self._file_doc.set(*section_1)
            r = FileDoc(self._filename).get("section 1")
            expected = "line 1\nline 2"
            self.assertEqual(expected, r)
        with self.subTest():
            section_2 = ("section 2", "line 3\nline 4")
            self._file_doc.set(*section_2)
            r = FileDoc(self._filename).get("section 2")
            expected = "line 3\nline 4"
            self.assertEqual(expected, r)
        with self.subTest():
            section_3 = Section("section 3", "line 5\nline 6")
            self._file_doc.set(*section_3)
            r = FileDoc(self._filename).get("section 3")
            expected = "line 5\nline 6"
            self.assertEqual(expected, r)

    def test_build_method(self):
        data = {"name": "alex", "pi": 3.14}
        self._file_doc.embed("section 1", data)
        self._file_doc.set("section 2", "line 1\nline 2")
        with self.subTest():
            r = FileDoc(self._filename).build("section 1")
            self.assertEqual(data, r)
        with self.assertRaises(ParadictError):
            FileDoc(self._filename).build("section 2")

    def test_build_config_method(self):
        data = {"name": "alex", "pi": 3.14}
        self._file_doc.embed("section 1", data)
        self._file_doc.set("section 2", "line 1\nline 2")
        with self.subTest():
            with self.assertRaises(ParadictError):
                FileDoc(self._filename).build_config()

    def test_embed_method(self):
        data = {"name": "alex", "pi": 3.14}
        self._file_doc.embed("section 1", data)
        r = FileDoc(self._filename).get("section 1")
        expected = 'name = "alex"\npi = 3.14'
        self.assertEqual(expected, r)

    def test_list_headers_method(self):
        r = self._file_doc.list_headers()
        expected = tuple()
        self.assertEqual(expected, r)

    def test_render_method(self):
        r = self._file_doc.render()
        expected = str()
        self.assertEqual(expected, r)

    def test_remove_method(self):
        # 1
        with self.subTest("Test 'remove' method without argument"):
            headers = tuple()
            try:
                self._file_doc.remove(headers)
            except Exception as e:
                self.assertTrue(False)
        # 2
        with self.subTest("Test 'remove' method with argument"):
            headers = ("header", )
            try:
                self._file_doc.remove(headers)
            except Exception as e:
                self.assertTrue(False)

    def test_clear_method(self):
        try:
            self._file_doc.clear()
        except Exception as e:
            self.assertTrue(False)


class TestFileDoc(unittest.TestCase):

    def setUp(self):
        file = tempfile.NamedTemporaryFile(delete=False)
        file.write(INIT_TEXT.encode("utf-8"))
        file.close()
        self._filename = file.name
        self._file_doc = FileDoc(self._filename)

    def tearDown(self):
        pathlib.Path(self._filename).unlink()

    def test_get_method(self):
        r = self._file_doc.get("section 1")
        expected = 'name = "alex"\npi = 3.14'
        self.assertEqual(expected, r)

    def test_get_lines_method(self):
        r = self._file_doc.get_lines("section 1")
        expected = ['name = "alex"', "pi = 3.14"]
        self.assertEqual(expected, r)

    def test_set_method(self):
        data = ['name = "alex"', 'pi = 0']
        self._file_doc.set("section 1", data)
        r = FileDoc(self._filename).get("section 1")
        expected = 'name = "alex"\npi = 0'
        self.assertEqual(expected, r)

    def test_build_method(self):
        with self.subTest():
            r = self._file_doc.build("section 1")
            expected = {"name": "alex", "pi": 3.14}
            self.assertEqual(expected, r)
        with self.assertRaises(ParadictError):
            self._file_doc.build("")

    def test_build_config_method(self):
        with self.assertRaises(ParadictError):
            FileDoc(self._filename).build_config()

    def test_embed_method(self):
        data = {"name": "alex", "pi": 0}
        self._file_doc.embed("section 1", data)
        r = FileDoc(self._filename).get("section 1")
        expected = 'name = "alex"\npi = 0'
        self.assertEqual(expected, r)

    def test_list_headers_method(self):
        r = self._file_doc.list_headers()
        expected = ("", "section 1", "section 2", "section 3")
        self.assertEqual(expected, r)

    def test_render_method(self):
        # 1
        with self.subTest("Render the entire doc"):
            r = self._file_doc.render()
            expected = INIT_TEXT
            self.assertEqual(expected, r)
        # 2
        with self.subTest("Render the unnamed section"):
            r = self._file_doc.render("")
            expected = "line 1\nline 2"
            self.assertEqual(expected, r)
        # 3
        with self.subTest("Render section 1"):
            r = self._file_doc.render("section 1")
            expected = """\
            [section 1]
            name = "alex"
            pi = 3.14"""
            self.assertEqual(dedent(expected), r)

    def test_remove_method(self):
        # 1
        with self.subTest("Test 'remove' method without argument"):
            headers = tuple()
            self._file_doc.remove(headers)
            r = self._file_doc.list_headers()
            expected = ("", "section 1", "section 2", "section 3")
            self.assertEqual(expected, r)
        # 2
        with self.subTest("Test 'remove' method with argument"):
            headers = ("section 1", )
            self._file_doc.remove(headers)
            r = FileDoc(self._filename).list_headers()
            expected = ("", "section 2", "section 3")
            self.assertEqual(expected, r)

    def test_clear_method(self):
        self._file_doc.clear()
        r = FileDoc(self._filename).list_headers()
        expected = tuple()
        self.assertEqual(expected, r)


class TestFileDocWithComment(unittest.TestCase):

    def setUp(self):
        text = """\
        # this is a comment
        pi = 3.14"""
        file = tempfile.NamedTemporaryFile(delete=False)
        file.write(dedent(text).encode("utf-8"))
        file.close()
        self._filename = file.name
        self._file_doc = FileDoc(self._filename)

    def tearDown(self):
        pathlib.Path(self._filename).unlink()

    def test_build_method(self):
        r = self._file_doc.build("")
        expected = {"pi": 3.14}
        self.assertEqual(expected, r)



class TestAutosaveMode(unittest.TestCase):

    def setUp(self):
        file = tempfile.NamedTemporaryFile(delete=False)
        file.close()
        self._filename = file.name
        self._file_doc = FileDoc(self._filename)

    def tearDown(self):
        pathlib.Path(self._filename).unlink()

    def test_set_method(self):
        section_1 = ("section 1", ["line 1", "line 2"])
        self._file_doc.set(*section_1)
        with self.subTest():
            r = FileDoc(self._filename).get("section 1")
            expected = "line 1\nline 2"
            self.assertEqual(expected, r)
        with self.subTest():
            self._file_doc.autosave = False
            section_2 = ("section 2", ["line 3", "line 4"])
            self._file_doc.set(*section_2)
            r = FileDoc(self._filename).get("section 2")
            self.assertIsNone(r)

    def test_embed_method(self):
        data = {"id": 42, "name": "alex"}
        self._file_doc.embed("section 1", data)
        with self.subTest():
            r = FileDoc(self._filename).build("section 1")
            self.assertEqual(data, r)
        with self.subTest():
            self._file_doc.autosave = False
            self._file_doc.embed("section 2", data)
            r = FileDoc(self._filename).build("section 2")
            self.assertIsNone(r)

    def test_remove_method(self):
        body = "line 1\nline 2"
        self._file_doc.set("section 1", body)
        with self.subTest():
            r = FileDoc(self._filename).get("section 1")
            self.assertEqual(body, r)
        with self.subTest():
            self._file_doc.autosave = False
            self._file_doc.remove("section 1")
            r = FileDoc(self._filename).get("section 1")
            self.assertEqual(body, r)

    def test_clear_method(self):
        body = "line 1\nline 2"
        self._file_doc.set("section 1", body)
        with self.subTest():
            r = FileDoc(self._filename).get("section 1")
            self.assertEqual(body, r)
        with self.subTest():
            self._file_doc.autosave = False
            self._file_doc.clear()
            r = FileDoc(self._filename).get("section 1")
            self.assertEqual(body, r)


class TestSaveMethod(unittest.TestCase):

    def setUp(self):
        file = tempfile.NamedTemporaryFile(delete=False)
        file.close()
        self._filename = file.name
        self._file_doc = FileDoc(self._filename, autosave=False)

    def tearDown(self):
        pathlib.Path(self._filename).unlink()

    def test(self):
        body = "line 1\nline 2"
        self._file_doc.set("section 1", body)
        with self.subTest("#1"):
            r = FileDoc(self._filename).get("section 1")
            self.assertIsNone(r)
        with self.subTest("#2"):
            self._file_doc.save()
            r = FileDoc(self._filename).get("section 1")
            self.assertEqual(body, r)


class TestLoadMethod(unittest.TestCase):

    def setUp(self):
        file = tempfile.NamedTemporaryFile(delete=False)
        file.close()
        self._filename = file.name
        self._file_doc = FileDoc(self._filename)

    def tearDown(self):
        pathlib.Path(self._filename).unlink()

    def test(self):
        new_file_doc = FileDoc(self._filename)
        new_file_doc.load()  # by default, lazy_loading is set to true, so...
        body = "line 1\nline 2"
        self._file_doc.set("section 1", body)
        with self.subTest("#1"):
            r = new_file_doc.get("section 1")
            self.assertIsNone(r)
        with self.subTest("#2"):
            new_file_doc.load()
            r = new_file_doc.get("section 1")
            self.assertEqual(body, r)


class TestLoadFromFileOperation(unittest.TestCase):

    def setUp(self):
        file = tempfile.NamedTemporaryFile(delete=False)
        file.write(INIT_TEXT.encode("utf-8"))
        file.close()
        self._filename = file.name
        self._file_doc = FileDoc(self._filename)

    def tearDown(self):
        pathlib.Path(self._filename).unlink()

    def test(self):
        self._file_doc.load_from(self._filename)
        r = FileDoc(self._filename).get("section 1")
        expected = 'name = "alex"\npi = 3.14'
        self.assertEqual(expected, r)


class TestSaveToFileOperation(unittest.TestCase):

    def setUp(self):
        file = tempfile.NamedTemporaryFile(delete=False)
        file.write(INIT_TEXT.encode("utf-8"))
        file.close()
        self._filename = file.name
        self._file_doc = FileDoc(self._filename)

    def tearDown(self):
        pathlib.Path(self._filename).unlink()

    def test(self):
        self._file_doc.save_to(self._filename)
        with open(self._filename, "r", encoding="utf-8") as file:
            r = file.read()
        expected = INIT_TEXT
        self.assertEqual(expected, r)


class TestFileDocWithSchema(unittest.TestCase):

    def setUp(self):
        file = tempfile.NamedTemporaryFile(delete=False)
        file.write(INIT_TEXT.encode("utf-8"))
        file.close()
        self._filename = file.name
        self._file_doc = FileDoc(self._filename, schema=SCHEMA)

    def tearDown(self):
        pathlib.Path(self._filename).unlink()

    def test_schema_property(self):
        r = self._file_doc.schema
        expected = SCHEMA
        self.assertEqual(expected, r)

    def test_validate_method(self):
        # 1
        with self.subTest("Validate the entire doc"):
            r = self._file_doc.is_valid()
            expected = False
            self.assertEqual(expected, r)
        # 2
        with self.subTest("Validate section 1 and section 2"):
            r = self._file_doc.is_valid("section 1", "section 2")
            expected = True
            self.assertEqual(expected, r)
        # 3
        with self.subTest("Validate unnamed section and section 3"):
            r = self._file_doc.is_valid("", "section 3")
            expected = False
            self.assertEqual(expected, r)


class TestFileDocWithEmptySchema(unittest.TestCase):

    def setUp(self):
        file = tempfile.NamedTemporaryFile(delete=False)
        file.write(INIT_TEXT.encode("utf-8"))
        file.close()
        self._filename = file.name
        self._file_doc = FileDoc(self._filename, schema=dict())

    def tearDown(self):
        pathlib.Path(self._filename).unlink()

    def test_schema_property(self):
        r = self._file_doc.schema
        expected = dict()
        self.assertEqual(expected, r)

    def test_validate_method(self):
        # 1
        with self.subTest("Validate the entire doc"):
            r = self._file_doc.is_valid()
            expected = True
            self.assertEqual(expected, r)
        # 2
        with self.subTest("Validate section 1 and section 2"):
            r = self._file_doc.is_valid("section 1", "section 2")
            expected = True
            self.assertEqual(expected, r)
        # 3
        with self.subTest("Validate unnamed section and section 3"):
            r = self._file_doc.is_valid("", "section 3")
            expected = True
            self.assertEqual(expected, r)


if __name__ == "__main__":
    unittest.main()
