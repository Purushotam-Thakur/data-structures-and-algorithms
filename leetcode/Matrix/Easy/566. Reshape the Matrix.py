from typing import List

from nose.tools import assert_list_equal


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        if m * n != r * c:
            return mat
        item = [y for x in mat for y in x]
        res = []
        for x in range(0, len(item), c):
            res.append(item[x:x + c])
        return res


class testSuits:

    @staticmethod
    def test(sol):
        assert_list_equal(sol([[1,2],[3,4]],1,4), [[1,2,3,4]])
        assert_list_equal(sol([[1,2],[3,4]],2,4),[[1,2],[3,4]])
        print('ALL TEST CASES PASSED')


s = Solution()
t = testSuits()
t.test(s.matrixReshape)
