import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def test_start(self):
        self.assertEqual(3, self.solution.maximumCount([-2, -1, -1, 1, 2, 3]))
        self.assertEqual(3, self.solution.maximumCount(
            [-3, -2, -1, 0, 0, 1, 2]))
        self.assertEqual(4, self.solution.maximumCount([5, 20, 66, 1314]))


if __name__ == "__main__":
    unittest.main()
