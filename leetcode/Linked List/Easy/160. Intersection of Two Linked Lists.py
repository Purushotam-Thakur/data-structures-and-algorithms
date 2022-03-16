
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        track = {}

        while headA:
            track[headA] = 1
            headA = headA.next
        while headB:
            if headB in track:
                return headB
            headB = headB.next
