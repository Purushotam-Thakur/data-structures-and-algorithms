from typing import List
from nose.tools import assert_equal


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        ans = 0

        for i in range(2, n):
            if nums[i - 1] - nums[i - 2] == nums[i] - nums[i - 1]:
                dp[i] = dp[i - 1] + 1
            ans += dp[i]
        return ans


class testSuits:

    @staticmethod
    def test(sol):
        assert_equal(sol([1,2,3,4]), 3)
        assert_equal(sol([1]), 0)
        print('ALL TEST CASES PASSED')


solObj = Solution()
t = testSuits()
t.test(solObj.numberOfArithmeticSlices)
