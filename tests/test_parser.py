import unittest
from braq.parser import get_header, is_header, parse, parse_compact


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

# for 'parse_iter()'
DICT_1 = {"":
              ["line 1",
               "line 2",
               ""],
          "section 1":
              ["line 3",
               "line 4",
               "",
               "line 5"],
          "section 2":
              ["",
               "line 6",
               ""]}

# for 'parse_iter()' function with end_of_stream == "line 6"
DICT_2 = {"":
              ["line 1",
               "line 2",
               ""],
          "section 1":
              ["line 3",
               "line 4",
               ""],
          "section 2":
              [""]}

# for 'parse()' function
DICT_3 = {"": "line 1\nline 2",
          "section 1": "line 3\nline 4\n\nline 5",
          "section 2": "\nline 6"}

# for 'parse()' function with end_of_stream == "line 6"
DICT_4 = {"": "line 1\nline 2",
          "section 1": "line 3\nline 4",
          "section 2": ""}


class TestParseFunction(unittest.TestCase):

    def test_empty_text(self):
        text = ""
        r = parse_compact(text)
        self.assertEqual(dict(), r)

    def test_text_with_sections(self):
        r = parse_compact(TEXT)
        self.assertEqual(DICT_3, r)

    def test_end_of_stream(self):
        r = parse_compact(TEXT, end_of_stream="line 6")
        self.assertEqual(DICT_4, r)


class TestParseIterativelyFunction(unittest.TestCase):

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


class TestParseClass(unittest.TestCase):

    def test(self):
        # this class is covered by the parse function tests
        self.assertTrue(True)


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


class TestCheckHeaderFunction(unittest.TestCase):

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


if __name__ == '__main__':
    unittest.main()
