import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def test_start(self):
        self.assertEqual(2, self.solution.findTheDistanceValue(
            [4, 5, 8], [10, 9, 1, 8], 2))
        self.assertEqual(2, self.solution.findTheDistanceValue(
            [1, 4, 2, 3], [-4, -3, 6, 10, 20, 30], 3))
        self.assertEqual(1, self.solution.findTheDistanceValue(
            [2, 1, 100, 3], [-5, -2, 10, -3, 7], 6))


if __name__ == "__main__":
    unittest.main()
