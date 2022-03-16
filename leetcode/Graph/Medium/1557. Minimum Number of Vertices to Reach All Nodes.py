from typing import List

from nose.tools import assert_list_equal


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        track = [0] * n

        for f, t in edges:
            track[t] += 1
        res = []
        for i in range(n):
            if track[i] == 0:
                res.append(i)
        return res


class testSuits:

    @staticmethod
    def test(sol):
        assert_list_equal(sol(6, [[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]), [0, 3])
        assert_list_equal(sol(5, [[0, 1], [2, 1], [3, 1], [1, 4], [2, 4]]), [0, 2, 3])
        print('ALL TEST CASES PASSED')


solObj = Solution()
t = testSuits()
t.test(solObj.findSmallestSetOfVertices)
