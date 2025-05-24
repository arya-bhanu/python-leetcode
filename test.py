import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def test_start(self):
        self.assertEqual(2, self.solution.countMaxOrSubsets([3, 1]))
        self.assertEqual(7, self.solution.countMaxOrSubsets([2, 2, 2]))
        self.assertEqual(6, self.solution.countMaxOrSubsets([3, 2, 1, 5]))


if __name__ == "__main__":
    unittest.main()
