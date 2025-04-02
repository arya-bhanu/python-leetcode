import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def test_start(self):
        self.assertEqual(
            [15, 1, 11, 22], self.solution.leftRightDifference([10, 4, 8, 3]))
        self.assertEqual(
            [0], self.solution.leftRightDifference([1]))


if __name__ == "__main__":
    unittest.main()
