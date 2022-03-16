from typing import List

from nose.tools import assert_equal


class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        track = 0
        t_lower = 0
        t_higher = 0

        for i in differences:
            track += i
            if track < t_lower:
                t_lower = track
            if track > t_higher:
                t_higher = track

        print(t_lower, t_higher)
        count = (upper - t_higher) - (lower - t_lower) + 1
        count = count if count > 0 else 0
        return count


class testSuits:

    @staticmethod
    def test(sol):
        assert_equal(sol([1, -3, 4], 1, 6), 2)
        assert_equal(sol([3, -4, 5, 1, -2], -4, 5), 4)
        assert_equal(sol([4, -7, 2], 3, 6), 0)
        assert_equal(sol([-40], -46, 53), 60)
        assert_equal(sol([83702,-5216], -82788, 14602), 13689)
        print('ALL TEST CASES PASSED')


s = Solution()
t = testSuits()
t.test(s.numberOfArrays)
