import unittest
from braq import (get_header, is_header, parse,
                  decode, render, exhaust_iterator, Section)


TEXT = """\
line 1
line 2

[section 1]
line 3
line 4


[section 2]

line 6

[section 1]
line 5"""

# for 'parse()'
DICT_1 = {"": ["line 1", "line 2", ""],
          "section 1": ["line 3", "line 4", "", "", "line 5"],
          "section 2": ["", "line 6", ""]}

# for 'parse()' function with end_of_stream == "line 6"
DICT_2 = {"": ["line 1", "line 2", ""],
          "section 1": ["line 3", "line 4", "", ""],
          "section 2": [""]}

# for 'decode()' function
DICT_3 = {"": ["line 1", "line 2"],
          "section 1": ["line 3", "line 4", "line 5"],
          "section 2": ["", "line 6"]}

# for 'decode()' function with end_of_stream == "line 6"
DICT_4 = {"": ["line 1", "line 2"],
          "section 1": ["line 3", "line 4"],
          "section 2": []}


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


class TestDecodeFunction(unittest.TestCase):

    def test_empty_text(self):
        text = ""
        r = decode(text)
        self.assertEqual(dict(), r)

    def test_text_with_sections(self):
        r = decode(TEXT)
        self.assertEqual(DICT_3, r)

    def test_end_of_stream(self):
        r = decode(TEXT, end_of_stream="line 6")
        self.assertEqual(DICT_4, r)


class TestParseFunction(unittest.TestCase):

    def test_empty_text(self):
        text = ""
        with self.assertRaises(StopIteration):
            next(parse(text))

    def test_text_with_sections(self):
        cache = dict()
        for header, body in parse(TEXT):
            if header not in cache:
                cache[header] = list()
            for line in body:
                cache[header].append(line)
        self.assertEqual(DICT_1, cache)

    def test_end_of_stream(self):
        cache = dict()
        for header, body in parse(TEXT, end_of_stream="line 6"):
            if header not in cache:
                cache[header] = list()
            for line in body:
                cache[header].append(line)
        self.assertEqual(DICT_2, cache)


class TestRenderFunction(unittest.TestCase):

    def test_with_no_sections(self):
        sections = tuple()
        r = render(sections)
        self.assertEqual("", r)

    def test_with_sections(self):
        sections = SECTION_0, SECTION_1, SECTION_2
        r = render(sections)
        self.assertEqual(TEXT_1, r)

    def test_spacing(self):
        sections = SECTION_0, SECTION_1, SECTION_2
        r = render(sections, spacing=0)
        self.assertEqual(TEXT_2, r)


class TestGetHeaderFunction(unittest.TestCase):

    def test_with_valid_line(self):
        expected = "my header"
        with self.subTest("line without trailing whitespace"):
            line = "[my header]"
            r = get_header(line)
            self.assertEqual(expected, r)
        with self.subTest("line with trailing whitespace"):
            line = "[my header] "
            r = get_header(line)
            self.assertEqual(expected, r)

    def test_with_invalid_line(self):
        with self.subTest():
            line = "[my header]x"
            r = get_header(line)
            self.assertIsNone(r)
        with self.subTest():
            line = " [my header]"
            r = get_header(line)
            self.assertIsNone(r)
        with self.subTest():
            line = "[my header"
            r = get_header(line)
            self.assertIsNone(r)
        with self.subTest():
            line = "my header]"
            r = get_header(line)
            self.assertIsNone(r)


class TestIsHeaderFunction(unittest.TestCase):

    def test_with_valid_line(self):
        with self.subTest("line without trailing whitespace"):
            line = "[my header]"
            r = is_header(line)
            self.assertTrue(r)
        with self.subTest("line with trailing whitespace"):
            line = "[my header] "
            r = is_header(line)
            self.assertTrue(r)

    def test_with_invalid_line(self):
        with self.subTest():
            line = "[my header]x"
            r = is_header(line)
            self.assertFalse(r)
        with self.subTest():
            line = " [my header]"
            r = is_header(line)
            self.assertFalse(r)
        with self.subTest():
            line = "[my header"
            r = is_header(line)
            self.assertFalse(r)
        with self.subTest():
            line = "my header]"
            r = is_header(line)
            self.assertFalse(r)


class TestExhaustIterator(unittest.TestCase):

    def test_iterator(self):
        my_iterator = iter([1, 2, 3, 4, 5])
        exhaust_iterator(my_iterator)
        with self.assertRaises(StopIteration):
            next(my_iterator)

    def test_empty_iterator(self):
        my_iterator = iter(list())
        exhaust_iterator(my_iterator)
        with self.assertRaises(StopIteration):
            next(my_iterator)


if __name__ == "__main__":
    unittest.main()
