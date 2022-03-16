from typing import List

from nose.tools import assert_list_equal


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # otherwise, there is overlap, so we merge the current and previous
                # intervals.
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged


class testSuits:

    @staticmethod
    def test(sol):
        assert_list_equal(sol([[1, 3], [2, 6], [8, 10], [15, 18]]), [[1, 6], [8, 10], [15, 18]])
        assert_list_equal(sol([[1, 4], [4, 5]]), [[1, 5]])
        print('ALL TEST CASES PASSED')


s = Solution()
t = testSuits()
t.test(s.merge)
