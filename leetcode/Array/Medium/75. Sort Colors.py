from typing import List
from nose.tools import assert_list_equal


class Solution:
    def sortColors(self, nums: List[int]) -> List[int]:
        """
        Do not return anything, modify nums in-place instead.
        """
        r, w, b = 0, 0, len(nums) - 1

        while w <= b:
            if nums[w] == 0:
                nums[r], nums[w] = nums[w], nums[r]
                r += 1
                w += 1
            elif nums[w] == 1:
                w += 1
            else:
                nums[w], nums[b] = nums[b], nums[w]
                b -= 1
        return nums


class testSuits:

    @staticmethod
    def test(sol):
        assert_list_equal(sol([2, 0, 2, 1, 1, 0]), [0, 0, 1, 1, 2, 2])
        assert_list_equal(sol([2, 0, 1]), [0, 1, 2])
        print('ALL TEST CASES PASSED')


s = Solution()
t = testSuits()
t.test(s.sortColors)
