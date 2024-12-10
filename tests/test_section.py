import unittest
from braq import Section


class TestSectionClass(unittest.TestCase):

    def test_empty_section(self):
        section = Section("section 1")
        with self.subTest():
            self.assertEqual("section 1", section.header)
            self.assertEqual(list(), section.body)
        with self.subTest():
            self.assertEqual("[section 1]", str(section))

    def test_unnamed_section(self):
        section = Section("", ["line 1", "line 2"])
        with self.subTest():
            self.assertEqual("", section.header)
            self.assertEqual(["line 1", "line 2"], section.body)
        with self.subTest():
            self.assertEqual("line 1\nline 2", str(section))

    def test_section_with_body_as_lines(self):
        section = Section("section 1", ["", "line 1", "line 2", ""])
        with self.subTest():
            self.assertEqual("section 1", section.header)
            self.assertEqual(["", "line 1", "line 2"], section.body)
        with self.subTest():
            self.assertEqual("[section 1]\n\nline 1\nline 2", str(section))

    def test_section_with_body_as_text(self):
        section = Section("section 1", "\nline 1\nline 2")
        with self.subTest():
            self.assertEqual("section 1", section.header)
            self.assertEqual(["", "line 1", "line 2"], section.body)
        with self.subTest():
            self.assertEqual("[section 1]\n\nline 1\nline 2", str(section))


if __name__ == "__main__":
    unittest.main()
