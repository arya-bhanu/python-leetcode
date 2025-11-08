import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def test_start(self):
        self.assertEqual(
            True, self.solution.checkIfPangram("thequickbrownfoxjumpsoverthelazydog")
        )
        self.assertEqual(False, self.solution.checkIfPangram("leetcode"))


if __name__ == "__main__":
    unittest.main()
