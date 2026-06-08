import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def test_start(self):
        self.assertEqual(
            [0, 2, 3, 4],
            self.solution.findThePrefixCommonArray([1, 3, 2, 4], [3, 1, 2, 4]),
        )
        self.assertEqual(
            [0, 1, 3], self.solution.findThePrefixCommonArray([2, 3, 1], [3, 1, 2])
        )


if __name__ == "__main__":
    unittest.main()
