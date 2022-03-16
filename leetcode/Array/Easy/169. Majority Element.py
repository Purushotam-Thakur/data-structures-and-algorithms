from typing import List

from nose.tools import assert_equal


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for n in nums:
            if count == 0:
                candidate = n
            count += (1 if candidate == n else -1)
        return candidate


class testSuits:

    @staticmethod
    def test(sol):
        assert_equal(sol([3, 2, 3, 3, 5, 3, 7]), 3)
        assert_equal(sol([3, 2, 3]), 3)
        assert_equal(sol([2, 2, 1, 1, 1, 2, 2]), 2)
        print('ALL TEST CASES PASSED')


s = Solution()
t = testSuits()
t.test(s.majorityElement)
