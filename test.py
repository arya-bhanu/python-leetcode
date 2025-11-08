import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def test_start(self):
        self.assertEqual(4, self.solution.arrayPairSum([1, 4, 3, 2]))
        self.assertEqual(9, self.solution.arrayPairSum([6, 2, 6, 5, 1, 2]))


if __name__ == "__main__":
    unittest.main()
