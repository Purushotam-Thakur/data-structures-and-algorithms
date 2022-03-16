from typing import List

from nose.tools import assert_equal


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        prev, max_diff = 0, 0

        for i in range(len(seats)):
            if seats[i]:
                if seats[prev]:
                    max_diff = max(max_diff, (i - prev) // 2)
                else:
                    max_diff = max(max_diff, i - prev)

                prev = i

        if seats[prev]:
            max_diff = max(max_diff, len(seats) - prev - 1)
        return max_diff


class testSuits:

    @staticmethod
    def test(sol):
        assert_equal(sol([1, 0, 0, 0, 1, 0, 1]), 2)
        assert_equal(sol([1, 0, 0, 0]), 3)
        assert_equal(sol([0, 1]), 1)
        print('ALL TEST CASES PASSED')


s = Solution()
t = testSuits()
t.test(s.maxDistToClosest)
