import heapq
from collections import Counter
from typing import List

from nose.tools import assert_list_equal


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums

        count = Counter[nums]

        return heapq.nlargest(k, count.keys(), key=count.get)


class testSuits:

    @staticmethod
    def test(sol):
        assert_list_equal(sol([1, 1, 1, 2, 2, 3], 2), [1, 2])
        assert_list_equal(sol([1], 1), [1])
        print('ALL TEST CASES PASSED')


solObj = Solution()
t = testSuits()
t.test(solObj.topKFrequent)
