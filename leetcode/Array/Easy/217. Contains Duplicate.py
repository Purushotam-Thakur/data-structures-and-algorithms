from typing import List

from nose.tools import assert_true, assert_false


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


class testSuits:

    @staticmethod
    def test(sol):
        assert_true(sol([1, 2, 3, 1]))
        assert_false(sol([1, 2, 3, 4]))
        assert_true(sol([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
        print('ALL TEST CASES PASSED')


solObj = Solution()
t = testSuits()
t.test(solObj.containsDuplicate)
