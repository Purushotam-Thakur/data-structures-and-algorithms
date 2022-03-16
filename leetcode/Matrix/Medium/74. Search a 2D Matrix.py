from typing import List

from nose.tools import assert_true, assert_false


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) < 1:
            return False

        r, c = len(matrix), len(matrix[0])
        lo, hi = 0, r * c - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            num = matrix[mid // c][mid % c]
            if num == target:
                return True
            elif num < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return False


class testSuits:

    @staticmethod
    def test(sol):
        assert_true(sol([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
        assert_false(sol([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))
        print('ALL TEST CASES PASSED')


s = Solution()
t = testSuits()
t.test(s.searchMatrix)
