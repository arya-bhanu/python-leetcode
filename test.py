import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def test_start(self):
        self.assertEqual(
            [3, 1, 4], self.solution.recoverOrder([3, 1, 2, 5, 4], [1, 3, 4])
        )
        self.assertEqual([5, 2], self.solution.recoverOrder([1, 4, 5, 3, 2], [2, 5]))


if __name__ == "__main__":
    unittest.main()
