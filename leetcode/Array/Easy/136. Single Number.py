from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        while len(nums) > 1:
            nums[0] ^= nums.pop()

        return nums.pop()
