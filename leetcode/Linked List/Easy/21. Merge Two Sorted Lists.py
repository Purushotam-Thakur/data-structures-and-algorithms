# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_list = ListNode()
        self.list = new_list

        while list1 and list2:
            if list1.val < list2.val:
                new_list.next = ListNode(list1.val)
                list1 = list1.next
            else:
                new_list.next = ListNode(list2.val)
                list2 = list2.next
            new_list = new_list.next

        if list1:
            new_list.next = list1
        if list2:
            new_list.next = list2
        return self.list.next
