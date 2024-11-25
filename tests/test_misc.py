import unittest
from braq import misc


class TestExhaustIterator(unittest.TestCase):

    def test_iterator(self):
        my_iterator = iter([1, 2, 3, 4, 5])
        misc.exhaust_iterator(my_iterator)
        with self.assertRaises(StopIteration):
            next(my_iterator)

    def test_empty_iterator(self):
        my_iterator = iter(list())
        misc.exhaust_iterator(my_iterator)
        with self.assertRaises(StopIteration):
            next(my_iterator)


if __name__ == "__main__":
    unittest.main()
