import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def test_start(self):
        self.assertEqual(
            "dcbaefd", self.solution.reversePrefix("abcdefd", "d"))
        self.assertEqual("zxyxxe", self.solution.reversePrefix("xyxzxe", "z"))
        self.assertEqual("abcd", self.solution.reversePrefix("abcd", "z"))
        self.assertEqual("shvdqeiygbnolmapfjcxtkuwzr", self.solution.reversePrefix(
            "rzwuktxcjfpamlonbgyieqdvhs", "s"))


if __name__ == "__main__":
    unittest.main()
