import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def test_start(self):
        self.assertEqual(True, self.solution.isPrefixString(
            "iloveleetcode", ["i", "love", "leetcode", "apples"]))
        self.assertEqual(False, self.solution.isPrefixString(
            "iloveleetcode", ["apples", "i", "love", "leetcode"]))


if __name__ == "__main__":
    unittest.main()
