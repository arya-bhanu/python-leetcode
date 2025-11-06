# Definition for singly-linked list.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        merged = ListNode()
        mergeP = merged
        # headMerged = merged
        head1 = list1
        head2 = list2
        while head1 or head2:
            val1 = None
            if head1:
                val1 = head1.val
            val2 = None
            if head2:
                val2 = head2.val
            if val1 and val2 and val1 < val2:
                obj = ListNode(val1)
                obj.next = ListNode(val2)
                head1 = head1.next
                head2 = head2.next
                mergeP.next = obj
                mergeP = obj.next
                continue
            if val1 and val2:
                obj = ListNode(val2)
                obj.next = ListNode(val1)
                head1 = head1.next
                head2 = head2.next
                mergeP.next = obj
                mergeP = obj.next
                continue
            if val1 is not None:
                obj = ListNode(val1)
                head1 = head1.next
                mergeP.next = obj
                mergeP = obj.next
                continue
            if val2 is not None:
                obj = ListNode(val2)
                head2 = head2.next
                mergeP.next = obj
                mergeP = obj.next
                continue
        return merged.next
