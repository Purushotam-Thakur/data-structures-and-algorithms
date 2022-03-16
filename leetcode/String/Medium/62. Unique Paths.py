from nose.tools import assert_equal


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n
        for i in range(m - 1):
            new_row = [1] * n
            for j in range(n - 2, -1, -1):
                new_row[j] = new_row[j + 1] + row[j]
            row = new_row
        return row[0]


class testSuits:

    @staticmethod
    def test(sol):
        assert_equal(sol(23, 12), 193536720)
        assert_equal(sol(3, 7), 28)
        assert_equal(sol(3, 2), 3)
        print('ALL TEST CASES PASSED')


s = Solution()
t = testSuits()
t.test(s.uniquePaths)
