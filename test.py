import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def test_start(self):
        self.assertEqual(
            3, self.solution.distributeCandies([1, 1, 2, 2, 3, 3]))
        self.assertEqual(
            2, self.solution.distributeCandies([1, 1, 2, 3]))
        self.assertEqual(
            1, self.solution.distributeCandies([6, 6, 6, 6]))


if __name__ == "__main__":
    unittest.main()
