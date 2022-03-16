from typing import List
from nose.tools import assert_equal


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n
        max_point = 2

        for i in range(n):
            for j in range(i + 1, n):
                count = 2
                for k in range(n):
                    if k != i and k != j:
                        if (points[i][1] - points[j][1]) * (points[i][0] - points[k][0]) == (
                                points[i][1] - points[k][1]) * (points[i][0] - points[j][0]):
                            count += 1
                max_point = max(max_point, count)

        return max_point


class testSuits:

    @staticmethod
    def test(sol):
        assert_equal(sol([[1, 1], [2, 2], [3, 3]]), 3)
        assert_equal(sol([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]), 4)
        print('ALL TEST CASES PASSED')


s = Solution()
t = testSuits()
t.test(s.maxPoints)
