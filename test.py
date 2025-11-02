import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def test_start(self):
        self.assertEqual(5, self.solution.numberOfPairs([1, 3, 4], [1, 3, 4], 1))
        self.assertEqual(2, self.solution.numberOfPairs([1, 2, 4, 12], [2, 4], 3))


if __name__ == "__main__":
    unittest.main()
