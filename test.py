import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def test_start(self):
        self.assertEqual(
            [5, 7, 2, 3, 2], self.solution.findArray([5, 2, 0, 3, 1]))
        self.assertEqual(
            [13], self.solution.findArray([13]))


if __name__ == "__main__":
    unittest.main()
