import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def test_start(self):
        self.assertEqual(2, self.solution.specialArray([3, 5]))
        self.assertEqual(-1, self.solution.specialArray([0, 0]))
        self.assertEqual(3, self.solution.specialArray([0, 4, 3, 0, 4]))
        self.assertEqual(-1, self.solution.specialArray([2, 3, 0, 2]))


if __name__ == "__main__":
    unittest.main()
