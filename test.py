import unittest
from main import Solution, ListNode


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def list_to_linked_list(self, arr):
        """Helper function to convert a list to a linked list"""
        if not arr:
            return None
        head = ListNode(arr[0])
        current = head
        for val in arr[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    def linked_list_to_list(self, head):
        """Helper function to convert a linked list to a list"""
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result

    def insertGreatestCommonDivisors(self, arr):
        """Wrapper to convert array input/output for easier testing"""
        head = self.list_to_linked_list(arr)
        original_head = head  # Keep reference to original head
        self.solution.insertGreatestCommonDivisors(head)
        return self.linked_list_to_list(original_head)

    def test_start(self):
        self.assertEqual(
            [18, 6, 6, 2, 10, 1, 3],
            self.insertGreatestCommonDivisors([18, 6, 10, 3]),
        )
        self.assertEqual([7], self.insertGreatestCommonDivisors([7]))


if __name__ == "__main__":
    unittest.main()
