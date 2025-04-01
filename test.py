import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def test_start(self):
        self.assertEqual(3, self.solution.findMaxK([-1, 2, -3, 3]))
        self.assertEqual(7, self.solution.findMaxK([-1, 10, 6, 7, -7, 1]))
        self.assertEqual(-1, self.solution.findMaxK([-10, 8, 6, 7, -2, -3]))


if __name__ == "__main__":
    unittest.main()
