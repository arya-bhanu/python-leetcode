import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def test_start(self):
        self.assertEqual(
            sorted([[], [1], [2], [1, 2], [3], [1, 3],
                   [2, 3], [1, 2, 3]], key=sorted),
            sorted(self.solution.subsets([1, 2, 3]), key=sorted)
        )
        self.assertEqual(
            sorted([[], [0]], key=sorted),
            sorted(self.solution.subsets([0]), key=sorted)
        )


if __name__ == "__main__":
    unittest.main()
