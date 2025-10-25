import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def test_start(self):
        self.assertEqual(
            1, self.solution.finalValueAfterOperations(["--X", "X++", "X++"])
        )
        self.assertEqual(
            3, self.solution.finalValueAfterOperations(["++X", "++X", "X++"])
        )
        self.assertEqual(
            0, self.solution.finalValueAfterOperations(["X++", "++X", "--X", "X--"])
        )


if __name__ == "__main__":
    unittest.main()
