import unittest
from extrapractice import search, binary_search


class SearchTest(unittest.TestCase):
    def checking_func(self, func):
        self.assertEqual(func([1, 2, 7, 15, 18], 7), 2)
        self.assertEqual(func([1, 2, 3, 4, 5], 6), None)
        self.assertEqual(func([1, 1, 1], 1), 0)

    def test_search(self):
        self.checking_func(search)

    def test_binary_search(self):
        self.checking_func(binary_search)


if __name__ == "__main__":
    unittest.main()
