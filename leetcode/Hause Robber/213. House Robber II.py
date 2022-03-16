from typing import List
from nose.tools import assert_equal


class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.choose_rob(nums[1:]), self.choose_rob(nums[:-1]))

    def choose_rob(self, nums: List[int]) -> int:
        rob1 = 0
        rob2 = 0

        for i in nums:
            temp = max(rob1 + i, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2


class testSuits:

    @staticmethod
    def test(sol):
        assert_equal(sol([2, 3, 2]), 3)
        assert_equal(sol([1, 2, 3, 1]), 4)
        assert_equal(sol([1, 2, 3]), 3)
        print('ALL TEST CASES PASSED')


s = Solution()
t = testSuits()
t.test(s.rob)
