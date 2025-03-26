import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def test_start(self):
        self.assertEqual([[1, 0, 0], [0, 1, 0], [1, 1, 1]], self.solution.flipAndInvertImage(
            [[1, 1, 0], [1, 0, 1], [0, 0, 0]]))
        self.assertEqual([[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1], [1, 0, 1, 0]], self.solution.flipAndInvertImage(
            [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]))


if __name__ == "__main__":
    unittest.main()
