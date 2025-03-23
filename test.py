import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def test_start(self):
        self.assertEqual([[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [
                         1, 4, 6, 4, 1]], self.solution.generate(5))
        self.assertEqual([[1]], self.solution.generate(1))


if __name__ == "__main__":
    unittest.main()
