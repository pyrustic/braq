import unittest


class TestImports(unittest.TestCase):

    def test_import_classes(self):
        try:
            # import classes
            from braq import Section
            from braq import Parser
            # import functions
            from braq import parse
            from braq import decode
            from braq import render
            from braq import is_header
            from braq import get_header
        except ImportError:
            self.assertTrue(False)


if __name__ == "__main__":
    unittest.main()
