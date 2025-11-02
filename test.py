import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def test_start(self):
        self.assertEqual(13, self.solution.scoreOfString("hello"))
        self.assertEqual(50, self.solution.scoreOfString("zaz"))


if __name__ == "__main__":
    unittest.main()
