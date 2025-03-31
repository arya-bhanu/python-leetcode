import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def test_start(self):
        self.assertEqual(9, self.solution.findKthPositive([2, 3, 4, 7, 11], 5))
        self.assertEqual(6, self.solution.findKthPositive([1, 2, 3, 4], 2))
        self.assertEqual(3, self.solution.findKthPositive([1, 2], 1))


if __name__ == "__main__":
    unittest.main()
