from typing import List

from nose.tools import assert_list_equal


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]
        for _ in range(rowIndex):
            res = [i + j for i, j in zip([0] + res, res + [0])]
        return res


class testSuits:

    @staticmethod
    def test(sol):
        assert_list_equal(sol(0), [1])
        assert_list_equal(sol(1), [1, 1])
        assert_list_equal(sol(2), [1, 2, 1])
        assert_list_equal(sol(3), [1, 3, 3, 1])
        print('ALL TEST CASES PASSED')


s = Solution()
t = testSuits()
t.test(s.getRow)
