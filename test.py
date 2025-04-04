import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def test_start(self):
        self.assertEqual([12, 10, 16, 13],
                         self.solution.decrypt([5, 7, 1, 4], 3))
        self.assertEqual([0, 0, 0, 0], self.solution.decrypt([1, 2, 3, 4], 0))
        self.assertEqual(
            [12, 5, 6, 13], self.solution.decrypt([2, 4, 9, 3], -2))


if __name__ == "__main__":
    unittest.main()
