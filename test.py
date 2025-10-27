import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def test_start(self):
        self.assertEqual(
            "100000100000-10-11101", self.solution.convertDateToBinary("2080-02-29")
        )
        self.assertEqual(
            "11101101100-1-1", self.solution.convertDateToBinary("1900-01-01")
        )


if __name__ == "__main__":
    unittest.main()
