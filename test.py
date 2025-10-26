import unittest
from main import Solution, ListNode


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def array_to_linkedlist(self, arr):
        """Convert an array to a linked list"""
        if not arr:
            return None

        head = ListNode(arr[0])
        current = head

        for i in range(1, len(arr)):
            current.next = ListNode(arr[i])
            current = current.next

        return head

    def linkedlist_to_array(self, head):
        """Convert a linked list to an array"""
        result = []
        current = head

        while current:
            result.append(current.val)
            current = current.next

        return result

    def test_case_1(self):
        """Test case: [0,3,1,0,4,5,2,0] -> [4,11]"""
        input_arr = [0, 3, 1, 0, 4, 5, 2, 0]
        expected_output = [4, 11]

        # Convert array to linked list
        head = self.array_to_linkedlist(input_arr)

        # Execute the function
        result_head = self.solution.mergeNodes(head)

        # Convert result back to array
        result_arr = self.linkedlist_to_array(result_head)

        self.assertEqual(result_arr, expected_output)

    def test_case_2(self):
        """Test case: [0,1,0,3,0,2,2,0] -> [1,3,4]"""
        input_arr = [0, 1, 0, 3, 0, 2, 2, 0]
        expected_output = [1, 3, 4]

        # Convert array to linked list
        head = self.array_to_linkedlist(input_arr)

        # Execute the function
        result_head = self.solution.mergeNodes(head)

        # Convert result back to array
        result_arr = self.linkedlist_to_array(result_head)

        self.assertEqual(result_arr, expected_output)

    # def test_single_segment(self):
    #     """Test case with single segment: [0,5,0] -> [5]"""
    #     input_arr = [0, 5, 0]
    #     expected_output = [5]

    #     head = self.array_to_linkedlist(input_arr)
    #     result_head = self.solution.mergeNodes(head)
    #     result_arr = self.linkedlist_to_array(result_head)

    #     self.assertEqual(result_arr, expected_output)

    # def test_multiple_single_values(self):
    #     """Test case: [0,1,0,2,0,3,0] -> [1,2,3]"""
    #     input_arr = [0, 1, 0, 2, 0, 3, 0]
    #     expected_output = [1, 2, 3]

    #     head = self.array_to_linkedlist(input_arr)
    #     result_head = self.solution.mergeNodes(head)
    #     result_arr = self.linkedlist_to_array(result_head)

    #     self.assertEqual(result_arr, expected_output)

    # def test_large_sum(self):
    #     """Test case with larger numbers: [0,10,20,30,0,5,5,0] -> [60,10]"""
    #     input_arr = [0, 10, 20, 30, 0, 5, 5, 0]
    #     expected_output = [60, 10]

    #     head = self.array_to_linkedlist(input_arr)
    #     result_head = self.solution.mergeNodes(head)
    #     result_arr = self.linkedlist_to_array(result_head)

    #     self.assertEqual(result_arr, expected_output)

    # def test_conversion_array_to_linkedlist(self):
    #     """Test array to linked list conversion"""
    #     arr = [1, 2, 3, 4, 5]
    #     head = self.array_to_linkedlist(arr)
    #     result = self.linkedlist_to_array(head)

    #     self.assertEqual(arr, result)

    # def test_conversion_empty_array(self):
    #     """Test conversion of empty array"""
    #     arr = []
    #     head = self.array_to_linkedlist(arr)

    #     self.assertIsNone(head)

    # def test_conversion_single_element(self):
    #     """Test conversion of single element array"""
    #     arr = [42]
    #     head = self.array_to_linkedlist(arr)
    #     result = self.linkedlist_to_array(head)

    #     self.assertEqual(arr, result)


if __name__ == "__main__":
    unittest.main()
