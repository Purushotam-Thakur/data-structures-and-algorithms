class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = {}
        lenLis, res = 0, 0

        for i in range(len(nums) - 1, -1, -1):
            maxLen, maxCount = 1, 1
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    length, count = dp[j]
                    if length + 1 > maxLen:
                        maxLen, maxCount = length + 1, count
                    elif length + 1 == maxLen:
                        maxCount += count
            if maxLen > lenLis:
                lenLis, res = maxLen, maxCount
            elif maxLen == lenLis:
                res += maxCount
            dp[i] = [maxLen, maxCount]

        return res
