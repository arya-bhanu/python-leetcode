import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def test_start(self):
        self.assertEqual([], self.solution.findPeaks([2, 4, 4]))
        self.assertEqual([1, 3], self.solution.findPeaks([1, 4, 3, 8, 5]))


if __name__ == "__main__":
    unittest.main()
