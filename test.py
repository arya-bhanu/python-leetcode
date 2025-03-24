import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def test_start(self):
        self.assertEqual(2, self.solution.arithmeticTriplets(
            [0, 1, 4, 6, 7, 10], 3))
        self.assertEqual(
            2, self.solution.arithmeticTriplets([4, 5, 6, 7, 8, 9], 2))


if __name__ == "__main__":
    unittest.main()
