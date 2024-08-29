import unittest
import pathlib
import tempfile
from braq.section import Section
from braq.fileio import write, read, read_iter


SECTION_0 = ("", "line 1\nline 2")
SECTION_1 = ("section 1", ["line 3", "line 4"])
SECTION_2 = (Section("section 2", ["line 5", "line 6"]))

# text with spacing == 1
TEXT_1 = """\
line 1
line 2

[section 1]
line 3
line 4

[section 2]
line 5
line 6"""

# text with spacing == 0
TEXT_2 = """\
line 1
line 2
[section 1]
line 3
line 4
[section 2]
line 5
line 6"""

# dict for testing 'read_iter()' function
DICT_1 = {"":
              ["line 1",
               "line 2",
               ""],
          "section 1":
              ["line 3",
               "line 4",
               ""],
          "section 2":
              ["line 5",
               "line 6"]}

# dict for testing 'read()' function
DICT_2 = {"": "line 1\nline 2",
          "section 1": "line 3\nline 4",
          "section 2": "line 5\nline 6"}

# dict for testing 'read_iter()' function with end_of_stream == "line 4"
DICT_3 = {"":
              ["line 1",
               "line 2",
               ""],
          "section 1":
              ["line 3"]}

# dict for testing 'read()' function with end_of_stream == "line 4"
DICT_4 = {"": "line 1\nline 2",
          "section 1": "line 3"}


class TestWriteFunction(unittest.TestCase):

    def setUp(self):
        file = tempfile.NamedTemporaryFile(delete=False)
        file.close()
        self._filename = file.name

    def tearDown(self):
        pathlib.Path(self._filename).unlink()

    def test_with_no_sections(self):
        sections = tuple()
        write(sections, dst=self._filename)
        with open(self._filename, "r", encoding="utf-8") as file:
            r = file.read()
        self.assertEqual("", r)

    def test_with_sections(self):
        sections = (SECTION_0, SECTION_1, SECTION_2)
        write(sections, dst=self._filename)
        with open(self._filename, "r", encoding="utf-8") as file:
            r = file.read()
        self.assertEqual(TEXT_1, r)

    def test_spacing(self):
        sections = (SECTION_0, SECTION_1, SECTION_2)
        write(sections, dst=self._filename, spacing=0)
        with open(self._filename, "r", encoding="utf-8") as file:
            r = file.read()
        self.assertEqual(TEXT_2, r)


class TestReadFunction(unittest.TestCase):

    def setUp(self):
        file = tempfile.NamedTemporaryFile(delete=False)
        file.close()
        self._filename = file.name

    def tearDown(self):
        pathlib.Path(self._filename).unlink()

    def test_with_empty_file(self):
        r = read(self._filename)
        self.assertEqual(dict(), r)

    def test_with_data(self):
        with open(self._filename, "w", encoding="utf-8") as file:
            file.write(TEXT_1)
        r = read(self._filename)
        self.assertEqual(DICT_2, r)

    def test_with_end_of_stream(self):
        with open(self._filename, "w", encoding="utf-8") as file:
            file.write(TEXT_1)
        r = read(self._filename, end_of_stream="line 4")
        self.assertEqual(DICT_4, r)


class TestReadIterativelyFunction(unittest.TestCase):

    def setUp(self):
        file = tempfile.NamedTemporaryFile(delete=False)
        file.close()
        self._filename = file.name

    def tearDown(self):
        pathlib.Path(self._filename).unlink()

    def test_with_empty_file(self):
        with self.assertRaises(StopIteration):
            next(read_iter(self._filename))

    def test_with_data(self):
        with open(self._filename, "w", encoding="utf-8") as file:
            file.write(TEXT_1)
        cache = dict()
        for header, body in read_iter(self._filename):
            if header not in cache:
                cache[header] = list()
            for line in body:
                cache[header].append(line)
        self.assertEqual(DICT_1, cache)

    def test_with_end_of_stream(self):
        with open(self._filename, "w", encoding="utf-8") as file:
            file.write(TEXT_1)
        cache = dict()
        for header, body in read_iter(self._filename,
                                      end_of_stream="line 4"):
            if header not in cache:
                cache[header] = list()
            for line in body:
                cache[header].append(line)
        self.assertEqual(DICT_3, cache)


if __name__ == '__main__':
    unittest.main()
