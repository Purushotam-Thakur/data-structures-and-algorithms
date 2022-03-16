from typing import List
from nose.tools import assert_equal


def min_swaps(arr: List[int]) -> int:
    n = len(arr)
    count_of_1 = arr.count(1)
    min_swaps_count = arr[0:count_of_1].count(0)
    final_min_swaps_count = arr[0:count_of_1].count(0)
    i = 1
    j = count_of_1
    while j < n:
        if arr[i - 1] == 0:
            min_swaps_count -= 1
        if arr[j] == 0:
            min_swaps_count += 1
        final_min_swaps_count = min(final_min_swaps_count, min_swaps_count)
        i += 1
        j += 1
    return final_min_swaps_count


class minSwapsTest:
    @staticmethod
    def test(sol):
        assert_equal(sol([1, 0, 1, 0, 1]), 1)
        assert_equal(sol([0, 0, 1, 0, 1, 1, 0, 0, 1]), 1)
        assert_equal(sol([1, 0, 1, 0, 1, 1]), 1)
        assert_equal(sol([1, 0, 1, 0, 1, 1, 0, 0, 1]), 2)
        assert_equal(sol([1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0]), 1)
        assert_equal(sol([1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0]), 1)
        assert_equal(sol([1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0]), 4)
        print('ALL TEST CASES PASSED')


t = minSwapsTest()
t.test(min_swaps)
