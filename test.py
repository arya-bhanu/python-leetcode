import unittest
from main import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def test_start(self):
        self.assertEqual(True, self.solution.containsNearbyDuplicate([1, 2, 3, 1], 3))
        self.assertEqual(True, self.solution.containsNearbyDuplicate([1, 0, 1, 1], 1))
        self.assertEqual(
            False, self.solution.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2)
        )


if __name__ == "__main__":
    unittest.main()
