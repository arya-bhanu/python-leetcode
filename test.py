import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def test_start(self):
        self.assertEqual(
            [2, 1], self.solution.findIntersectionValues([2, 3, 2], [1, 2])
        )
        self.assertEqual(
            [3, 4],
            self.solution.findIntersectionValues([4, 3, 2, 3, 1], [2, 2, 5, 2, 3, 6]),
        )
        self.assertEqual(
            [0, 0], self.solution.findIntersectionValues([3, 4, 2, 3], [1, 5])
        )
        self.assertEqual(
            [4, 2],
            self.solution.findIntersectionValues(
                [24, 28, 7, 27, 7, 27, 9, 24, 9, 10], [12, 29, 9, 7, 5]
            ),
        )


if __name__ == "__main__":
    unittest.main()
