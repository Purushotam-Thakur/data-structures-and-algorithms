from collections import Counter
from typing import List

from nose.tools import assert_equal


class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        track = Counter()
        l = len(nums)
        for i, n in enumerate(nums):
            if n == key and i + 1 < l:
                track[nums[i + 1]] += 1
        return track.most_common(1)[0][0]


class Solution1:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        track = {}
        res = None
        m_c = 0

        for i in range(len(nums) - 1):
            if nums[i] == key:
                if nums[i + 1] in track:
                    track[nums[i + 1]] += 1
                else:
                    track[nums[i + 1]] = 1
                if track[nums[i + 1]] > m_c:
                    res = nums[i + 1]
                    m_c = track[nums[i + 1]]
        return res


class testSuits:

    @staticmethod
    def test(sol):
        assert_equal(sol([1, 100, 200, 1, 100], 1), 100)
        assert_equal(sol([2, 2, 2, 2, 3], 2), 2)
        print('ALL TEST CASES PASSED')


s = Solution()
s1 = Solution1()
t = testSuits()
t.test(s.mostFrequent)
t.test(s1.mostFrequent)
