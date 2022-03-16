from typing import List

from nose.tools import assert_list_equal


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1;
                    r -= 1
        return res


class testSuits:

    @staticmethod
    def test(sol):
        assert_list_equal(sol([-1, 0, 1, 2, -1, -4]), [(-1, -1, 2), (-1, 0, 1)])
        assert_list_equal(sol([]), [])
        assert_list_equal(sol([0]), [])
        print('ALL TEST CASES PASSED')


s = Solution()
t = testSuits()
t.test(s.threeSum)
