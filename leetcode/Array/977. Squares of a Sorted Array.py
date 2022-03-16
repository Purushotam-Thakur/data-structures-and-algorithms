from typing import List
from nose.tools import assert_equal


def sorted_squares(nums: List[int]) -> List[int]:
    res = [0] * len(nums)
    l = 0
    c = r = len(nums) - 1

    while l <= r:
        ln, rn = abs(nums[l]), abs(nums[r])
        if ln > rn:
            res[r - l] = ln * ln
            l += 1
        else:
            res[r - l] = rn * rn
            r -= 1

    return res


class sorted_squares_test:

    @staticmethod
    def test(sol):
        assert_equal(sol([-4, -1, 0, 3, 10]), [0, 1, 9, 16, 100])
        print('ALL TEST CASES PASSED')


t = sorted_squares_test()
t.test(sorted_squares)
