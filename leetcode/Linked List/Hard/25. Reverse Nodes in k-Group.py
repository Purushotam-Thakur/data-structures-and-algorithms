
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = track = ListNode()

        while head:
            count = 0
            rev_track = rev = ListNode()
            cur_head = head
            while count < k and head:
                rev.val = head.val
                temp = ListNode()
                temp.next = rev
                rev = temp
                head = head.next
                count += 1
            if count == k:
                track.next = rev.next
                track = rev_track
            else:
                track.next = cur_head
        return dummy.next


