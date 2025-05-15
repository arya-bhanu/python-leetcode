import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def test_start(self):
        self.assertEqual(
            [-1, 3, -1], self.solution.nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))
        self.assertEqual(
            [3, -1], self.solution.nextGreaterElement([2, 4], [1, 2, 3, 4]))
        self.assertEqual([7, 7, 7, 7, 7], self.solution.nextGreaterElement(
            [1, 3, 5, 2, 4], [6, 5, 4, 3, 2, 1, 7]))


if __name__ == "__main__":
    unittest.main()
