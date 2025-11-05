import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def test_start(self):
        self.assertEqual(148, self.solution.reverseDegree("abc"))
        self.assertEqual(160, self.solution.reverseDegree("zaza"))


if __name__ == "__main__":
    unittest.main()
