from typing import List
from nose.tools import assert_true, assert_false


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l = len(nums)
        last_index = l - 1

        for i in range(l - 1, -1, -1):
            if i + nums[i] >= last_index:
                last_index = i

        return last_index == 0


class testSuits:

    @staticmethod
    def test(sol):
        assert_true(sol([2, 3, 1, 1, 4]))
        assert_false(sol([3, 2, 1, 0, 4]))
        print('ALL TEST CASES PASSED')


s = Solution()
t = testSuits()
t.test(s.canJump)
