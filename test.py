import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def test_start(self):
        self.assertEqual(1, self.solution.singleNumber([2, 2, 1]))
        self.assertEqual(4, self.solution.singleNumber([4, 1, 2, 1, 2]))
        self.assertEqual(1, self.solution.singleNumber([1]))


if __name__ == "__main__":
    unittest.main()
