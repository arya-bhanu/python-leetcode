# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        firstHead = head
        ptr = head
        sum = 0
        while ptr:
            if ptr.val != 0:
                sum += ptr.val
            elif ptr.val == 0 and sum != 0:
                firstHead.val = sum
                firstHead.next = ptr
                firstHead = ptr
                sum = 0
            ptr = ptr.next
        return head
