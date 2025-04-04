import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def test_start(self):
        self.assertEqual(
            12, self.solution.countKConstraintSubstrings("10101", 1))
        self.assertEqual(
            25, self.solution.countKConstraintSubstrings("1010101", 2))
        self.assertEqual(
            15, self.solution.countKConstraintSubstrings("11111", 1))


if __name__ == "__main__":
    unittest.main()
