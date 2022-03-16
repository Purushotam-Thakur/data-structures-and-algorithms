from typing import List

from nose.tools import assert_equal


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        res = right = 0
        intervals.sort(key=lambda a: (a[0], -a[1]))
        for i, j in intervals:
            if j > right:
                res += 1
            right = max(right, j)
        return res


class testSuits:

    @staticmethod
    def test(sol):
        assert_equal(sol([[1, 4], [3, 6], [2, 8]]), 2)
        assert_equal(sol([[1, 4], [2, 3]]), 1)
        print('ALL TEST CASES PASSED')


solObj = Solution()
t = testSuits()
t.test(solObj.removeCoveredIntervals)
