from typing import List
from nose.tools import assert_equal


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)

        if n < 1:
            return 0
        graph = {}

        for i in range(n):
            if arr[i] in graph:
                graph[arr[i]].append(i)
            else:
                graph[arr[i]] = [i]

        layer = [0]
        visited = {0}
        step = 0

        while layer:
            nex = []

            for node in layer:
                if node == n - 1:
                    return step

                for j in graph[arr[node]]:
                    if j not in visited:
                        visited.add(j)
                        nex.append(j)
                graph[arr[node]].clear()

                for j in [node - 1, node + 1]:
                    if 0 <= j < n and j not in visited:
                        visited.add(j)
                        nex.append(j)

            layer = nex
            step += 1

        return -1


class testSuits:

    @staticmethod
    def test(sol):
        assert_equal(sol([100, -23, -23, 404, 100, 23, 23, 23, 3, 404]), 3)
        assert_equal(sol([7]), 0)
        assert_equal(sol([7, 6, 9, 6, 9, 6, 9, 7]), 1)
        print('ALL TEST CASES PASSED')


s = Solution()
t = testSuits()
t.test(s.minJumps)
