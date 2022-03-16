from nose.tools import assert_equal


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high + 1) // 2 - low // 2


class testSuits:

    @staticmethod
    def test(sol):
        assert_equal(sol(3, 7), 3)
        assert_equal(sol(8, 10), 1)
        print('ALL TEST CASES PASSED')


s = Solution()
t = testSuits()
t.test(s.countOdds)
