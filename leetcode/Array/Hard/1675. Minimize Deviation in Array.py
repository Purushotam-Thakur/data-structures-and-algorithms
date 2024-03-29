import heapq
from typing import List

from nose.tools import assert_equal


class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        pq = []
        for a in nums:
            heapq.heappush(pq, [a // (a & -a), a])

        res = float('inf')
        ma = max(a for a, a0 in pq)

        while len(pq) == len(nums):
            a, a0 = heapq.heappop(pq)
            res = min(res, ma - a)

            if a % 2 == 1 or a < a0:
                ma = max(ma, a * 2)
                heapq.heappush(pq, [a * 2, a0])
        return res


class testSuits:

    @staticmethod
    def test(sol):
        assert_equal(sol([1, 2, 3, 4]), 1)
        assert_equal(sol([4, 1, 5, 20, 3]), 3)
        print('ALL TEST CASES PASSED')


solObj = Solution()
t = testSuits()
t.test(solObj.minimumDeviation)
