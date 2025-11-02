import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def test_start(self):
        self.assertEqual(4, self.solution.minMovesToSeat([3, 1, 5], [2, 7, 4]))
        self.assertEqual(7, self.solution.minMovesToSeat([4, 1, 5, 9], [1, 3, 2, 6]))
        self.assertEqual(4, self.solution.minMovesToSeat([2, 2, 6, 6], [1, 3, 2, 6]))


if __name__ == "__main__":
    unittest.main()
