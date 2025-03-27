import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def test_start(self):
        self.assertEqual(
            [0, 0, 1, 1], self.solution.transformArray([4, 3, 2, 1]))
        self.assertEqual(
            [0, 0, 1, 1, 1], self.solution.transformArray([1, 5, 1, 4, 2]))


if __name__ == "__main__":
    unittest.main()
