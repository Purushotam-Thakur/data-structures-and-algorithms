import math
from typing import List
from nose.tools import assert_equal


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            middle = (left + right) // 2
            hour_spent = 0

            for pile in piles:
                hour_spent += math.ceil(pile / middle)

            if hour_spent > h:
                left = middle + 1
            else:
                right = middle

        return right


class testSuits:

    @staticmethod
    def test(sol):
        assert_equal(sol([3, 6, 7, 11], 8), 4)
        assert_equal(sol([30, 11, 23, 4, 20], 5), 30)
        assert_equal(sol([30, 11, 23, 4, 20], 6), 23)
        print('ALL TEST CASES PASSED')


s = Solution()
t = testSuits()
t.test(s.minEatingSpeed)
