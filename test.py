import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def test_start(self):
        self.assertEqual(5, self.solution.largestPerimeter([2, 1, 2]))
        self.assertEqual(0, self.solution.largestPerimeter([1, 2, 1, 10]))


if __name__ == "__main__":
    unittest.main()
