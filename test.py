import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def test_start(self):
        self.assertEqual([3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0],
                         self.solution.shortestToChar("loveleetcode", "e"))
        self.assertEqual(
            [3, 2, 1, 0], self.solution.shortestToChar("aaab", "b"))


if __name__ == "__main__":
    unittest.main()
