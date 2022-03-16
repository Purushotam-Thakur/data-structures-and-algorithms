# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        res = None

        while head:
            temp = ListNode(head.val)
            temp.next = res
            res = temp
            head = head.next
        return res

    def reverseList1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        stack = []
        while head:
            stack.append(head.val)
            head = head.next

        if stack:
            x = self.next = ListNode(stack.pop())

        while stack:
            x.next = ListNode(stack.pop())
            x = x.next
        return self.next