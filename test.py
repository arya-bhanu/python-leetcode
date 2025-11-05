import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def test_start(self):
        self.assertEqual(3, self.solution.minimumOperations([1, 2, 3, 4]))
        self.assertEqual(0, self.solution.minimumOperations([3, 6, 9]))


if __name__ == "__main__":
    unittest.main()
