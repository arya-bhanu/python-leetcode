import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def test_start(self):
        self.assertEqual(
            [4, 0, 1, 1, 3], self.solution.smallerNumbersThanCurrent([8, 1, 2, 2, 3])
        )
        self.assertEqual(
            [2, 1, 0, 3], self.solution.smallerNumbersThanCurrent([6, 5, 4, 8])
        )
        self.assertEqual(
            [0, 0, 0, 0], self.solution.smallerNumbersThanCurrent([7, 7, 7, 7])
        )


if __name__ == "__main__":
    unittest.main()
