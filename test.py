import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def test_start(self):
        self.assertEqual(3, self.solution.maxDepth("(1+(2*3)+((8)/4))+1"))
        self.assertEqual(3, self.solution.maxDepth("(1)+((2))+(((3)))"))
        self.assertEqual(3, self.solution.maxDepth("()(())((()()))"))
        self.assertEqual(3, self.solution.maxDepth(
            "()(())((()((((4(ART())))))))"))


if __name__ == "__main__":
    unittest.main()
