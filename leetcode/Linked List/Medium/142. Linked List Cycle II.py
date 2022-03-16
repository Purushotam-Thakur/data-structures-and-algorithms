

# Definition for singly-linked list.
from nose.tools import assert_equal


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        else:
            return None

        while head != slow:
            slow = slow.next
            head = head.next
        return head


class testSuits:

    @staticmethod
    def test(sol):
        assert_equal(sol(19))
        assert_equal(sol(2))
        print('ALL TEST CASES PASSED')


s = Solution()
t = testSuits()
t.test(s.isHappy)
