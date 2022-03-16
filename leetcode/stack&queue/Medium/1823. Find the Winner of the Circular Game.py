from nose.tools import assert_equal


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        res = 0

        for i in range(1, n + 1):
            res = (res + k) % i
        return res + 1


class testSuits:

    @staticmethod
    def test(sol):
        assert_equal(sol(5, 2), 3)
        assert_equal(sol(6, 5), 1)
        print('ALL TEST CASES PASSED')


solObj = Solution()
t = testSuits()
t.test(solObj.findTheWinner)
