import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def test_start(self):
        self.assertEqual(
            2, self.solution.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"])
        )
        self.assertEqual(1, self.solution.uniqueMorseRepresentations(["a"]))


if __name__ == "__main__":
    unittest.main()
