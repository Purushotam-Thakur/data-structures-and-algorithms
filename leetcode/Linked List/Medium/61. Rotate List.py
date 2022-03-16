# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        length = 1
        lastNode = head

        while lastNode.next:
            lastNode = lastNode.next
            length += 1

        k = k % length
        lastNode.next = head

        tempNode = head
        for _ in range(length - k - 1):
            tempNode = tempNode.next

        ans = tempNode.next
        tempNode.next = None
        return ans
