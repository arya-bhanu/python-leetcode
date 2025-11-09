import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def test_start(self):
        self.assertEqual(
            [2, 4], self.solution.findMissingAndRepeatedValues([[1, 3], [2, 2]])
        )
        self.assertEqual(
            [9, 5],
            self.solution.findMissingAndRepeatedValues(
                [[9, 1, 7], [8, 9, 2], [3, 4, 6]]
            ),
        )


if __name__ == "__main__":
    unittest.main()
