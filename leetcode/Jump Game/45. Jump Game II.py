from typing import List
from nose.tools import assert_equal


class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        left = right = 0

        while right < len(nums) - 1:
            max_step = 0
            for j in range(left, right + 1):
                max_step = max(max_step, j + nums[j])
            left = right + 1
            right = max_step
            res += 1
        return res


class testSuits:

    @staticmethod
    def test(sol):
        assert_equal(sol([2, 3, 1, 1, 4]), 2)
        assert_equal(sol([2, 3, 0, 1, 4]), 2)
        print('ALL TEST CASES PASSED')


s = Solution()
t = testSuits()
t.test(s.jump)
