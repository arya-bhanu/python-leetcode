import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def test_start(self):
        self.assertEqual(8, self.solution.countNegatives(
            [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]))
        self.assertEqual(0, self.solution.countNegatives(
            [[3, 2], [1, 0]]))


if __name__ == "__main__":
    unittest.main()
