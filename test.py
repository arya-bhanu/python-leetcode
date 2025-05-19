import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def test_start(self):
        self.assertEqual([9, 5, 3, 10, 10, 12, 14], self.solution.pivotArray(
            [9, 12, 5, 10, 14, 3, 10], 10))
        self.assertEqual([-3, 2, 4, 3], self.solution.pivotArray(
            [-3, 4, 3, 2], 2))


if __name__ == "__main__":
    unittest.main()
