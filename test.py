import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def test_start(self):
        self.assertCountEqual(
            [2], self.solution.intersection([1, 2, 2, 1], [2, 2]))
        self.assertCountEqual(
            [9, 4], self.solution.intersection([4, 9, 5], [9, 4, 9, 8, 4]))


if __name__ == "__main__":
    unittest.main()
