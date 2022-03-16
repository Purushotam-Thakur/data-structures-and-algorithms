from functools import lru_cache
from typing import List

from nose.tools import assert_true


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)

        @lru_cache(None)
        def dp(i, j):
            if i > j:
                return 0

            parity = (j - n - n) % 2
            if parity == 1:
                return max(piles[i] + dp(i + 1, j), piles[j] + dp(i, j - 1))
            else:
                return min(piles[i] + dp(i + 1, j), piles[j] + dp(i, j - 1))

        return dp(0, n - 1)


class testSuits:

    @staticmethod
    def test(sol):
        assert_true(sol([5, 3, 4, 5]))
        assert_true(sol([3, 7, 2, 3]))
        print('ALL TEST CASES PASSED')


s = Solution()
t = testSuits()
t.test(s.stoneGame)
