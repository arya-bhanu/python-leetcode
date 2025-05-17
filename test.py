import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def test_start(self):
        self.assertEqual(
            [4, 5, 2, 7], self.solution.sortArrayByParityII([4, 2, 5, 7]))
        self.assertEqual([2, 3], self.solution.sortArrayByParityII([2, 3]))


if __name__ == "__main__":
    unittest.main()
