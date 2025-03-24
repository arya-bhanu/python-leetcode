import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def test_start(self):
        self.assertEqual(5.5, self.solution.minimumAverage(
            [7, 8, 3, 4, 15, 13, 4, 1]))
        self.assertEqual(
            5.5, self.solution.minimumAverage([1, 9, 8, 3, 10, 5]))
        self.assertEqual(5.0, self.solution.minimumAverage([1, 2, 3, 7, 8, 9]))


if __name__ == "__main__":
    unittest.main()
