from functools import lru_cache
from typing import List
from nose.tools import assert_equal


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        @lru_cache
        def dp(i):
            if i >= len(questions): return 0
            points, jump = questions[i][0], questions[i][1]
            return max(dp(i + 1), points + dp(i + jump + 1))

        return dp(0)


class testSuits:

    @staticmethod
    def test(sol):
        assert_equal(sol([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]), 7)
        assert_equal(sol([[3, 2], [4, 3], [4, 4], [2, 5]]), 5)
        assert_equal(sol([[21, 5], [92, 3], [74, 2], [39, 4], [58, 2], [5, 5], [49, 4], [65, 3]]), 157)
        assert_equal(sol([[1,1],[2,2],[3,3],[4,4],[5,5]]), 7)
        assert_equal(sol([[43,5]]), 43)
        print('ALL TEST CASES PASSED')


s = Solution()
t = testSuits()
t.test(s.mostPoints)
