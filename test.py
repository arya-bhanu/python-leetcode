import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def test_start(self):
        self.assertEqual("1[.]1[.]1[.]1", self.solution.defangIPaddr("1.1.1.1"))
        self.assertEqual(
            "255[.]100[.]50[.]0", self.solution.defangIPaddr("255.100.50.0")
        )


if __name__ == "__main__":
    unittest.main()
