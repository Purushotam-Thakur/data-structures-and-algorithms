from typing import List

from nose.tools import assert_equal


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_length = 0
        count = 0
        track = {0: 0}

        for i, n in enumerate(nums, 1):
            if n == 0:
                count -= 1
            else:
                count += 1

            if count in track:
                max_length = max(max_length, i - track[count])
            else:
                track[count] = i
        return max_length


class testSuits:

    @staticmethod
    def test(sol):
        assert_equal(sol([0, 0, 1, 0, 0, 0, 1, 1]), 6)
        assert_equal(sol([0, 1]), 2)
        assert_equal(sol([0, 1, 0]), 2)
        print('ALL TEST CASES PASSED')


s = Solution()
t = testSuits()
t.test(s.findMaxLength)
