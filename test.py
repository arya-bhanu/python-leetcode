import unittest
from main import Solution, ListNode


def array_to_list(arr):
    """Convert a Python array to a linked list."""
    if not arr:
        return None

    head = ListNode(arr[0])
    current = head
    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next

    return head


def list_to_array(head):
    """Convert a linked list to a Python array."""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next

    return result


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def test_start(self):
        # # Test case 1: [1,2,4] + [1,3,4] should equal [1,1,2,3,4,4]
        # list1 = array_to_list([1, 2, 4])
        # list2 = array_to_list([1, 3, 4])
        # merged = self.solution.mergeTwoLists(list1, list2)
        # self.assertEqual([1, 1, 2, 3, 4, 4], list_to_array(merged))

        # # Test case 2: [] + [] should equal []
        # list1 = array_to_list([])
        # list2 = array_to_list([])
        # merged = self.solution.mergeTwoLists(list1, list2)
        # self.assertEqual([], list_to_array(merged))

        # # Test case 3: [] + [0] should equal [0]
        # list1 = array_to_list([])
        # list2 = array_to_list([0])
        # merged = self.solution.mergeTwoLists(list1, list2)
        # self.assertEqual([0], list_to_array(merged))

        # list1 = array_to_list([2])
        # list2 = array_to_list([1])
        # merged = self.solution.mergeTwoLists(list1, list2)
        # self.assertEqual([1, 2], list_to_array(merged))

        list1 = array_to_list([5])
        list2 = array_to_list([1, 2, 4])
        merged = self.solution.mergeTwoLists(list1, list2)
        self.assertEqual([1, 2, 4, 5], list_to_array(merged))


if __name__ == "__main__":
    unittest.main()
