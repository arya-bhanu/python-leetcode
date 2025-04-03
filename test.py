import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def test_start(self):
        self.assertEqual("abc", self.solution.clearDigits("abc"))
        self.assertEqual("", self.solution.clearDigits("cb34"))
        self.assertEqual("556", self.solution.clearDigits("cb34x4556"))


if __name__ == "__main__":
    unittest.main()
