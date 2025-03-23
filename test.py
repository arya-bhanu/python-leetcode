import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def test_start(self):
        self.assertEqual(2, self.solution.findNumbers([12, 345, 2, 6, 7896]))
        self.assertEqual(1, self.solution.findNumbers([555, 901, 482, 1771]))


if __name__ == "__main__":
    unittest.main()
