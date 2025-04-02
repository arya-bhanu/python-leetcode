import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def test_start(self):
        self.assertEqual(6, self.solution.pivotInteger(8))
        self.assertEqual(1, self.solution.pivotInteger(1))
        self.assertEqual(-1, self.solution.pivotInteger(4))


if __name__ == "__main__":
    unittest.main()
