from typing import List

from nose.tools import assert_equal


class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        nums = sorted(list(set(nums)))
        l = len(nums)

        if nums[l - 1] < k + l:
            return (l + k) * (l + k + 1) // 2 - sum(nums)

        lt, rt = 0, l - 1

        while lt < rt:
            mid = (lt + rt) // 2
            if nums[mid] - mid <= k:
                lt = mid + 1
            else:
                rt = mid
        return (lt + k) * (lt + k + 1) // 2 - sum(nums[:lt])


class testSuits:

    @staticmethod
    def test(sol):
        assert_equal(sol([1, 4, 25, 10, 25], 2), 5)
        assert_equal(sol([5, 6], 6), 25)
        print('ALL TEST CASES PASSED')


solObj = Solution()
t = testSuits()
t.test(solObj.minimalKSum)
