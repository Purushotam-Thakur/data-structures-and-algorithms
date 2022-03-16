from typing import List

from nose.tools import assert_equal


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        row = len(mat)
        total = 0

        for n in range(row):
            if row - 1 - n != n:
                total += mat[row - 1 - n][n]
            total += mat[n][n]

        return total


class testSuits:

    @staticmethod
    def test(sol):
        assert_equal(sol([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 25)
        assert_equal(sol([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]), 8)
        assert_equal(sol([[5]]), 5)
        print('ALL TEST CASES PASSED')


s = Solution()
t = testSuits()
t.test(s.diagonalSum)
