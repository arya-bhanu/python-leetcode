import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def test_start(self):
        self.assertEqual(11, self.solution.subarraySum([2, 3, 1]))
        self.assertEqual(13, self.solution.subarraySum([3, 1, 1, 2]))


if __name__ == "__main__":
    unittest.main()
