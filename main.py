# Definition for singly-linked list.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertGreatestCommonDivisors(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        ptr = head
        while ptr.next:
            left = max(ptr.val, ptr.next.val)
            right = min(ptr.val, ptr.next.val)

            ptr.next = ListNode(self.gcd(left, right), ptr.next)

            # shift
            ptr = ptr.next.next
        return head

    def gcd(self, left, right):
        while right != 0:
            r = left % right
            left = right
            right = r
        return left
