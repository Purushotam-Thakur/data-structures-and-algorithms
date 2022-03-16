class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        track = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    track[i] = max(track[i], 1 + track[j])

        return max(track)

