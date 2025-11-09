import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def test_start(self):
        self.assertEqual(7, self.solution.numberOfPoints([[3, 6], [1, 5], [4, 7]]))
        self.assertEqual(7, self.solution.numberOfPoints([[1, 3], [5, 8]]))


if __name__ == "__main__":
    unittest.main()
