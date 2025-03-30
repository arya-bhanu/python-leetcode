import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def test_start(self):
        self.assertEqual(
            [1, 2], self.solution.targetIndices([1, 2, 5, 2, 3], 2))
        self.assertEqual([3], self.solution.targetIndices([1, 2, 5, 2, 3], 3))
        self.assertEqual([4], self.solution.targetIndices([1, 2, 5, 2, 3], 5))


if __name__ == "__main__":
    unittest.main()
