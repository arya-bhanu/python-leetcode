import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def test_start(self):
        self.assertEqual(2, self.solution.missingNumber([3, 0, 1]))
        self.assertEqual(2, self.solution.missingNumber([0, 1]))
        self.assertEqual(8, self.solution.missingNumber(
            [9, 6, 4, 2, 3, 5, 7, 0, 1]))


if __name__ == "__main__":
    unittest.main()
