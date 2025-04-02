import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def test_start(self):
        self.assertEqual("s'teL ekat edoCteeL tsetnoc", self.solution.reverseWords(
            "Let's take LeetCode contest"))
        self.assertEqual("rM gniD", self.solution.reverseWords("Mr Ding"))


if __name__ == "__main__":
    unittest.main()
