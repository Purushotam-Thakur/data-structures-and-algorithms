from collections import defaultdict
from math import log
from typing import List

from nose.tools import assert_equal


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = defaultdict(int)
        max_n = 0
        for n in nums:
            points[n] += n
            max_n = max(max_n, n)

        two_back = one_back = 0
        l = len(points)
        if max_n < l + l * log(n, 2):
            one_back = points[1]
            for num in range(2, max_n + 1):
                two_back, one_back = one_back, max(one_back, two_back + points[num])
        else:
            elements = sorted(points.keys())
            one_back = points[elements[0]]
            for i in range(1, len(elements)):
                curr_element = elements[i]
                if curr_element == elements[i - 1] + 1:
                    two_back, one_back = one_back, max(one_back, two_back + points[curr_element])
                else:
                    two_back, one_back = one_back, one_back + points[curr_element]

        return one_back


class testSuits:

    @staticmethod
    def test(sol):
        assert_equal(sol([3, 4, 2]), 6)
        assert_equal(sol([2, 2, 3, 3, 3, 4]), 9)
        print('ALL TEST CASES PASSED')


solObj = Solution()
t = testSuits()
t.test(solObj.deleteAndEarn)
