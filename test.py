import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def test_start(self):
        self.assertEqual(
            [4, 2, 4, 2, 3], self.solution.finalPrices([8, 4, 6, 2, 3]))
        self.assertEqual(
            [1, 2, 3, 4, 5], self.solution.finalPrices([1, 2, 3, 4, 5]))
        self.assertEqual(
            [9, 0, 1, 6], self.solution.finalPrices([10, 1, 1, 6]))


if __name__ == "__main__":
    unittest.main()
