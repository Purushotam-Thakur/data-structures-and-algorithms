import math
from functools import lru_cache
from typing import List

from nose.tools import assert_equal


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        @lru_cache(None)
        def dp(amt):
            if amt == 0:
                return 0

            ans = math.inf

            for coin in coins:
                if amt >= coin:
                    ans = min(ans, dp(amt - coin) + 1)

            return ans

        ans = dp(amount)

        return ans if ans != math.inf else -1


class testSuits:

    @staticmethod
    def test(sol):
        assert_equal(sol([1, 2, 5], 11), 3)
        assert_equal(sol([2], 3), -1)
        assert_equal(sol([1], 0), 0)
        print('ALL TEST CASES PASSED')


s = Solution()
t = testSuits()
t.test(s.coinChange)
