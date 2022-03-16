from typing import List

from nose.tools import assert_equal


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]


class testSuits:

    @staticmethod
    def test(sol):
        assert_equal(sol([3, 2, 1, 5, 6, 4], 2), 5)
        assert_equal(sol([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4)
        print('ALL TEST CASES PASSED')


solObj = Solution()
t = testSuits()
t.test(solObj.findKthLargest)
