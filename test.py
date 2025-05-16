import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def test_start(self):
        self.assertEqual([[1, 6], [2, 3], [3, 2], [4, 6]], self.solution.mergeArrays(
            [[1, 2], [2, 3], [4, 5]], [[1, 4], [3, 2], [4, 1]]))
        self.assertEqual([[1, 3], [2, 4], [3, 6], [4, 3], [5, 5]], self.solution.mergeArrays(
            [[2, 4], [3, 6], [5, 5]], [[1, 3], [4, 3]]))


if __name__ == "__main__":
    unittest.main()
