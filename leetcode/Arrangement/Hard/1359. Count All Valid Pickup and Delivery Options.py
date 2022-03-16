from nose.tools import assert_equal


class Solution:
    def countOrders(self, n: int) -> int:
        MOD = 1_000_000_007
        ans = 1
        for i in range(1,n+1):
            ans = ans*i
            ans = ans*(2*i-1)
            ans %=MOD
        return ans


class testSuits:

    @staticmethod
    def test(sol):
        assert_equal(sol(1), 1)
        assert_equal(sol(2), 6)
        assert_equal(sol(10), 850728840)
        print('ALL TEST CASES PASSED')


s = Solution()
t = testSuits()
t.test(s.countOrders)
