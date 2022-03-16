from typing import List
from nose.tools import assert_true, assert_false


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if start < 0 or start >= len(arr) or arr[start] < 0:
            return False
        arr[start] *= -1

        return arr[start] == 0 or self.canReach(arr, start + arr[start]) or self.canReach(arr, start - arr[start])


class testSuits:

    @staticmethod
    def test(sol):
        assert_true(sol([4, 2, 3, 0, 3, 1, 2], 5))
        assert_true(sol([4, 2, 3, 0, 3, 1, 2], 0))
        assert_false(sol([3, 0, 2, 1, 2], 2))
        print('ALL TEST CASES PASSED')


s = Solution()
t = testSuits()
t.test(s.canReach)
