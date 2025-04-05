import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def test_start(self):
        self.assertEqual([1, 2], self.solution.fairCandySwap([1, 1], [2, 2]))
        self.assertEqual([1, 2], self.solution.fairCandySwap([1, 2], [2, 3]))
        self.assertEqual([2, 3], self.solution.fairCandySwap([2], [1, 3]))
        self.assertEqual(
            [5, 4], self.solution.fairCandySwap([1, 2, 5], [2, 4]))


if __name__ == "__main__":
    unittest.main()
