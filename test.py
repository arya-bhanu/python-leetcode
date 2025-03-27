import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def test_start(self):
        self.assertEqual(
            True, self.solution.canMakeArithmeticProgression([3, 5, 1]))
        self.assertEqual(
            False, self.solution.canMakeArithmeticProgression([1, 2, 4]))


if __name__ == "__main__":
    unittest.main()
