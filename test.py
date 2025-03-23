import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def test_isPrefix(self):
        self.assertEqual(0, self.solution.testMethod())


if __name__ == "__main__":
    unittest.main()
