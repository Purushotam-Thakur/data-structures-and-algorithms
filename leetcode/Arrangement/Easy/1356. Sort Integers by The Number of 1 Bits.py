from typing import List

from nose.tools import assert_list_equal


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda a: [bin(a).count('1'), a])


class testSuits:

    @staticmethod
    def test(sol):
        assert_list_equal(sol([0, 1, 2, 3, 4, 5, 6, 7, 8]), [0, 1, 2, 4, 8, 3, 5, 6, 7])
        assert_list_equal(sol([1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]),
                          [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024])
        print('ALL TEST CASES PASSED')


solObj = Solution()
t = testSuits()
t.test(solObj.sortByBits)
