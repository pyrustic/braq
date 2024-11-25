import unittest
from braq.section import render, Section


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


class TestSectionClass(unittest.TestCase):

    def test_empty_section(self):
        section = Section("section 1")
        with self.subTest():
            self.assertEqual("section 1", section.header)
            self.assertEqual("", section.body)
        with self.subTest():
            self.assertEqual("[section 1]", str(section))

    def test_unnamed_section(self):
        section = Section("", ["line 1", "line 2", ""])
        with self.subTest():
            self.assertEqual("", section.header)
            self.assertEqual("line 1\nline 2", section.body)
        with self.subTest():
            self.assertEqual("line 1\nline 2", str(section))

    def test_section_with_body_as_lines(self):
        section = Section("section 1", ["", "line 1", "line 2", ""])
        with self.subTest():
            self.assertEqual("section 1", section.header)
            self.assertEqual("\nline 1\nline 2", section.body)
        with self.subTest():
            self.assertEqual("[section 1]\n\nline 1\nline 2", str(section))

    def test_section_with_body_as_text(self):
        section = Section("section 1", "\nline 1\nline 2\n")
        with self.subTest():
            self.assertEqual("section 1", section.header)
            self.assertEqual("\nline 1\nline 2", section.body)
        with self.subTest():
            self.assertEqual("[section 1]\n\nline 1\nline 2", str(section))


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


if __name__ == '__main__':
    unittest.main()
