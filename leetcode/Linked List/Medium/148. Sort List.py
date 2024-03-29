# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        start = slow.next
        slow.next = None
        l, r = self.sortList(head), self.sortList(start)
        return self.merge(l, r)

    def merge(self, l, r):
        if not l or not r:
            return l or r

        res = curr = ListNode(0)

        while r and l:
            if r.val < l.val:
                curr.next = r
                r = r.next
            else:
                curr.next = l
                l = l.next
            curr = curr.next
        curr.next = l or r
        return res.next
