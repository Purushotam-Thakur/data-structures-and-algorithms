

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return

        count = 0
        track = head
        rev = ListNode()
        left = left_track = ListNode()

        while track:
            rev.val = track.val
            left_track.val = track.val
            temp = ListNode(0)
            temp.next = rev
            rev = temp
            track = track.next
            left_track.next = ListNode()
            left_track = left_track.next
            count += 1
        total_ite = count // 2

        rev = rev.next
        for i in range(total_ite):
            head.val = left.val
            head = head.next
            head.val = rev.val
            head = head.next
            left = left.next
            rev = rev.next

        if count % 2 != 0:
            head.val = left.val
