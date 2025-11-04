import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def test_start(self):
        self.assertEqual([0, 4, 1, 3, 2], self.solution.diStringMatch("IDID"))
        self.assertEqual([0, 1, 2, 3], self.solution.diStringMatch("III"))
        self.assertEqual([3, 2, 0, 1], self.solution.diStringMatch("DDI"))


if __name__ == "__main__":
    unittest.main()
