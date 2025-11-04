import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def test_start(self):
        self.assertEqual(4, self.solution.countKDifference([1, 2, 2, 1], 1))
        self.assertEqual(0, self.solution.countKDifference([1, 3], 3))
        self.assertEqual(3, self.solution.countKDifference([3, 2, 1, 5, 4], 2))


if __name__ == "__main__":
    unittest.main()
