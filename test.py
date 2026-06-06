import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def test_start(self):
        self.assertEqual(True, self.solution.uniqueOccurrences([1, 2, 2, 1, 1, 3]))
        self.assertEqual(False, self.solution.uniqueOccurrences([1, 2]))
        self.assertEqual(
            True, self.solution.uniqueOccurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0])
        )


if __name__ == "__main__":
    unittest.main()
