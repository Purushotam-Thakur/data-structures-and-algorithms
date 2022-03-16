from typing import List

from nose.tools import assert_equal
from sortedcontainers import SortedList


class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        pos = [0] * len(nums1)
        for idx, v in enumerate(nums2):
            pos[v] = idx

        pos_b, pre_a = SortedList([pos[nums1[0]]]), [0]
        for a in nums1[1:]:
            pos_b.add(pos[a])
            pre_a.append(pos_b.bisect_left(pos[a]))

        pos_b, suf_a = SortedList([pos[nums1[-1]]]), [0]
        for a in reversed(nums1[:len(nums1) - 1]):
            idx = pos_b.bisect(pos[a])
            suf_a.append(len(pos_b) - idx)
            pos_b.add(pos[a])
        suf_a.reverse()

        ans = 0

        for x, y in zip(pre_a, suf_a):
            ans += x * y
        return ans


class Solution1:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        track = set()

        def unique_triplet(path, nums):
            nonlocal track
            if len(path) > 3:
                return

            if len(path) == 3:
                check = '-'.join(str(a) for a in path)
                track.add(check)
                return

            for i in range(len(nums)):
                unique_triplet(path + [nums[i]], nums[i + 1:])

        res = set()

        def matchTriplet(path, nums):
            nonlocal res
            if len(path) > 3:
                return
            if len(path) == 3:
                check = '-'.join(str(a) for a in path)
                if check in track:
                    if check in res:
                        print(check)
                    res.add(check)
                return
            for i in range(len(nums)):
                matchTriplet(path + [nums[i]], nums[i + 1:])

        unique_triplet([], nums1)
        matchTriplet([], nums2)

        return len(res)


class testSuits:

    @staticmethod
    def test(sol):
        assert_equal(sol([2, 0, 1, 3], [0, 1, 2, 3]), 1)
        assert_equal(sol([4, 0, 1, 3, 2], [4, 1, 0, 2, 3]), 4)
        assert_equal(sol([12, 2, 1, 10, 7, 6, 13, 9, 11, 4, 5, 3, 14, 15, 8, 0],
                         [9, 11, 10, 4, 5, 2, 1, 8, 7, 3, 12, 13, 6, 15, 14, 0]), 156)
        assert_equal(sol([13, 14, 10, 2, 12, 3, 9, 11, 15, 8, 4, 7, 0, 6, 5, 1],
                         [8, 7, 9, 5, 6, 14, 15, 10, 2, 11, 4, 13, 3, 12, 1, 0]), 77)
        print('ALL TEST CASES PASSED')


solObj = Solution()
solObj1 = Solution1()
t = testSuits()
t.test(solObj.goodTriplets)
t.test(solObj1.goodTriplets)
