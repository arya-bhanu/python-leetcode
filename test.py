import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def test_start(self):
        self.assertEqual(5, self.solution.lengthOfLastWord("Hello World"))
        self.assertEqual(
            4, self.solution.lengthOfLastWord("   fly me   to   the moon  ")
        )
        self.assertEqual(6, self.solution.lengthOfLastWord("luffy is still joyboy"))


if __name__ == "__main__":
    unittest.main()
