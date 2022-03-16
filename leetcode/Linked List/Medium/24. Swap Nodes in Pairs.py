
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        d = ListNode(0)
        d.next = head
        c = d
        while c.next and c.next.next:
            f = c.next
            s = c.next.next
            c.next = s
            f.next = s.next
            s.next = f
            c = c.next.next
        return d.next
