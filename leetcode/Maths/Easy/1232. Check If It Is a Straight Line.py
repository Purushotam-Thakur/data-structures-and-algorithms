from typing import List

from nose.tools import assert_true, assert_false


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        (x1, y1), (x2, y2) = coordinates[:2]
        for (x, y) in coordinates:
            if (y2 - y1) * (x1 - x) != (y1 - y) * (x2 - x1):
                return False
        return True


class testSuits:

    @staticmethod
    def test(sol):
        assert_true(sol([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]))
        assert_false(sol([[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]))
        print('ALL TEST CASES PASSED')


s = Solution()
t = testSuits()
t.test(s.checkStraightLine)
