from typing import List, Optional

from nose.tools import assert_list_equal


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        amount = len(lists)
        interval = 1

        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge_2_lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else None

    def merge_2_lists(self, l1, l2):
        head = track = ListNode(0)

        while l1 and l2:
            if l1.val <= l2.val:
                track.next = l1
                l1 = l1.next
            else:
                track.next = l2
                l2 = l2.next
            track = track.next
        if l1:
            track.next = l1
        else:
            track.next = l2

        return head.next


class testSuits:

    @staticmethod
    def test(sol):
        assert_list_equal(sol([[1, 4, 5], [1, 3, 4], [2, 6]]), [1, 1, 2, 3, 4, 4, 5, 6])
        assert_list_equal(sol([[]]), [])
        assert_list_equal(sol([]), [])
        print('ALL TEST CASES PASSED')


s = Solution()
t = testSuits()
t.test(s.mergeKLists)
