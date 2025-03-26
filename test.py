import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def test_start(self):
        self.assertEqual("ada", self.solution.firstPalindrome(
            ["abc", "car", "ada", "racecar", "cool"]))
        self.assertEqual("racecar", self.solution.firstPalindrome(
            ["notapalindrome", "racecar"]))
        self.assertEqual("", self.solution.firstPalindrome(
            ["def", "ghi"]))


if __name__ == "__main__":
    unittest.main()
