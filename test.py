import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def test_start(self):
        self.assertEqual(
            "this is a secret",
            self.solution.decodeMessage(
                "the quick brown fox jumps over the lazy dog", "vkbs bs t suepuv"
            ),
        )
        self.assertEqual(
            "the five boxing wizards jump quickly",
            self.solution.decodeMessage(
                "eljuxhpwnyrdgtqkviszcfmabo", "zwx hnfx lqantp mnoeius ycgk vcnjrdb"
            ),
        )


if __name__ == "__main__":
    unittest.main()
