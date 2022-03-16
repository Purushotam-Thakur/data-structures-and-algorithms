from collections import defaultdict
from typing import List

from nose.tools import assert_list_equal


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        direct_child = defaultdict(list)
        for x, y in edges:
            direct_child[x].append(y)

        ans = [[] for _ in range(n)]

        def dfs(x, curr):
            for ch in direct_child[curr]:
                if ans[ch] and ans[ch][-1] == x:
                    continue
                ans[ch].append(x)
                dfs(x, ch)

        for i in range(n):
            dfs(i, i)

        return ans


class testSuits:

    @staticmethod
    def test(sol):
        assert_list_equal(sol(8, [[0, 3], [0, 4], [1, 3], [2, 4], [2, 7], [3, 5], [3, 6], [3, 7], [4, 6]]),
                          [[], [], [], [0, 1], [0, 2], [0, 1, 3], [0, 1, 2, 3, 4], [0, 1, 2, 3]])
        assert_list_equal(sol(5, [[0, 1], [0, 2], [0, 3], [0, 4], [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]),
                          [[], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3]])
        print('ALL TEST CASES PASSED')


solObj = Solution()
t = testSuits()
t.test(solObj.getAncestors)
