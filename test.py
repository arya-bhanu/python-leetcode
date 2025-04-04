import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def test_start(self):
        self.assertEqual(
            False, self.solution.checkAlmostEquivalent("aaaa", "bccb"))
        self.assertEqual(
            True, self.solution.checkAlmostEquivalent("abcdeef", "abaaacc"))
        self.assertEqual(True, self.solution.checkAlmostEquivalent(
            "cccddabba", "babababab"))
        self.assertEqual(False, self.solution.checkAlmostEquivalent(
            "zzzyyy", "iiiiii"))


if __name__ == "__main__":
    unittest.main()
