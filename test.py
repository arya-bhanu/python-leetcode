import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def test_start(self):
        self.assertEqual(-4, self.solution.alternatingSum([1, 3, 5, 7]))
        self.assertEqual(100, self.solution.alternatingSum([100]))


if __name__ == "__main__":
    unittest.main()
