import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def test_start(self):
        self.assertEqual(
            "()()()", self.solution.removeOuterParentheses("(()())(())"))
        self.assertEqual(
            "()()()()(())", self.solution.removeOuterParentheses("(()())(())(()(()))"))
        self.assertEqual("", self.solution.removeOuterParentheses("()()"))


if __name__ == "__main__":
    unittest.main()
