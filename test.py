import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def test_start(self):
        self.assertEqual(
            [10, 9], self.solution.minSubsequence([4, 3, 10, 9, 8]))
        self.assertEqual(
            [7, 7, 6], self.solution.minSubsequence([4, 4, 7, 6, 7]))
        self.assertEqual(
            [7], self.solution.minSubsequence([7]))


if __name__ == "__main__":
    unittest.main()
