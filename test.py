import unittest
from main import Solution, ListNode


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def list_to_linked_list(self, arr):
        """Convert a Python list to a linked list (ListNode)"""
        if not arr:
            return None
        head = ListNode(arr[0])
        current = head
        for val in arr[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    def linked_list_to_list(self, node):
        """Convert a linked list (ListNode) to a Python list"""
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result

    def test_start(self):
        # Test case 1: [2,4,3] + [5,6,4] = [7,0,8]
        l1 = self.list_to_linked_list([2, 4, 3])
        l2 = self.list_to_linked_list([5, 6, 4])
        result = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual([7, 0, 8], self.linked_list_to_list(result))

        # Test case 2: [0] + [0] = [0]
        l1 = self.list_to_linked_list([0])
        l2 = self.list_to_linked_list([0])
        result = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual([0], self.linked_list_to_list(result))

        # Test case 3: [9,9,9,9,9,9,9] + [9,9,9,9] = [8,9,9,9,0,0,0,1]
        l1 = self.list_to_linked_list([9, 9, 9, 9, 9, 9, 9])
        l2 = self.list_to_linked_list([9, 9, 9, 9])
        result = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual([8, 9, 9, 9, 0, 0, 0, 1], self.linked_list_to_list(result))


if __name__ == "__main__":
    unittest.main()
