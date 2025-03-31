import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def test_start(self):
        self.assertEqual([2, 0, 3], self.solution.kWeakestRows([[1, 1, 0, 0, 0],
                                                                [1, 1, 1, 1, 0],
                                                                [1, 0, 0, 0, 0],
                                                                [1, 1, 0, 0, 0],
                                                                [1, 1, 1, 1, 1]], 3))
        self.assertEqual([0, 2], self.solution.kWeakestRows([[1, 0, 0, 0],
                                                            [1, 1, 1, 1],
                                                             [1, 0, 0, 0],
                                                             [1, 0, 0, 0]], 2))


if __name__ == "__main__":
    unittest.main()
