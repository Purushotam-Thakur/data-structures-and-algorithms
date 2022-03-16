from nose.tools import assert_true, assert_false


class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False]*(n+1)
        for i in range(n+1):
            if dp[i]:
                continue
            p = int(n**.5)
            for j in range(1, p+1):
                if i+j*j <=n:
                    dp[i+j*j] = True
                else:
                    break
        return dp[n]


class testSuits:

    @staticmethod
    def test(sol):
        assert_true(sol(1))
        assert_false(sol(2))
        assert_true(sol(4))
        print('ALL TEST CASES PASSED')


s = Solution()
t = testSuits()
t.test(s.winnerSquareGame)
