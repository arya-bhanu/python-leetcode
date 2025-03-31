import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def test_start(self):
        self.assertEqual([2, 3, 4], self.solution.answerQueries(
            [4, 5, 2, 1], [3, 10, 21]))
        self.assertEqual([0], self.solution.answerQueries([2, 3, 4, 5], [1]))
        self.assertEqual([1, 0, 0, 1, 1, 0, 0, 0], self.solution.answerQueries(
            [624082], [972985, 564269, 607119, 693641, 787608, 46517, 500857, 140097]))


if __name__ == "__main__":
    unittest.main()
