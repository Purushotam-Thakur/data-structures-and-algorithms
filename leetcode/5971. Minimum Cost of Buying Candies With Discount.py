from typing import List
from nose.tools import assert_equal


class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        n = len(cost)
        total = 0

        if n < 3:
            return sum(cost)

        for i in range(n - 1, -1, -3):
            total += cost[i]
            if i - 1 >= 0:
                total += cost[i - 1]
        return total


class testSuits:

    @staticmethod
    def test(sol):
        assert_equal(sol([1, 2, 3]), 5)
        assert_equal(sol([1]), 1)
        assert_equal(sol([3,3,3,1]), 7)
        print('ALL TEST CASES PASSED')


s = Solution()
t = testSuits()
t.test(s.minimumCost)
