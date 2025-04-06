import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def test_start(self):
        self.assertEqual([1, 1, 3], self.solution.minOperations("110"))
        self.assertEqual([11, 8, 5, 4, 3, 4],
                         self.solution.minOperations("001011"))


if __name__ == "__main__":
    unittest.main()
