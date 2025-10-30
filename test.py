import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def test_start(self):
        self.assertEqual(
            [1, 0, 0, 2, 3, 0, 0, 4],
            self.solution.duplicateZeros([1, 0, 2, 3, 0, 4, 5, 0]),
        )
        self.assertEqual([1, 2, 3], self.solution.duplicateZeros([1, 2, 3]))


if __name__ == "__main__":
    unittest.main()
