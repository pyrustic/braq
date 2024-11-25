import unittest


class TestImports(unittest.TestCase):

    def test_import_classes(self):
        try:
            # import classes
            from braq import Document
            from braq import FileDoc
            from braq import Section
            from braq import Parser
            from braq import TypeRef
            # import functions
            from braq import parse
            from braq import parse_iter
            from braq import render
            from braq import read
            from braq import read_iter
            from braq import write
            from braq import load_config
            from braq import dump_config
            from braq import check_header
            from braq import get_header
        except ImportError:
            self.assertTrue(False)


if __name__ == "__main__":
    unittest.main()
