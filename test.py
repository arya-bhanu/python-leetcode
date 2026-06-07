import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def test_start(self):
        self.assertEqual(2, self.solution.maxDistinct("abab"))
        self.assertEqual(4, self.solution.maxDistinct("abcd"))
        self.assertEqual(1, self.solution.maxDistinct("aaaa"))


if __name__ == "__main__":
    unittest.main()
