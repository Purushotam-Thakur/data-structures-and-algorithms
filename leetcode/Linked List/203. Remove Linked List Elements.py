# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head

        self.list = ListNode('')
        self.list.next = head
        prev = self.list

        while head:
            if head.val == val:
                prev.next = prev.next.next
            else:
                prev = head
            head = head.next
        return self.list.next