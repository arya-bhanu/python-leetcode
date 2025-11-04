import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def test_start(self):
        self.assertEqual("efcfe", self.solution.makeSmallestPalindrome("egcfe"))
        self.assertEqual("abba", self.solution.makeSmallestPalindrome("abcd"))
        self.assertEqual("neven", self.solution.makeSmallestPalindrome("seven"))


if __name__ == "__main__":
    unittest.main()
