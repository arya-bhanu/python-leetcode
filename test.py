import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def test_start(self):
        self.assertEqual(
            ["Mary", "Emma", "John"],
            self.solution.sortPeople(["Mary", "John", "Emma"], [180, 165, 170]),
        )
        self.assertEqual(
            ["Bob", "Alice", "Bob"],
            self.solution.sortPeople(["Alice", "Bob", "Bob"], [155, 185, 150]),
        )


if __name__ == "__main__":
    unittest.main()
