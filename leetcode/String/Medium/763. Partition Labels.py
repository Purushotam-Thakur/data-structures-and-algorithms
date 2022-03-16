from typing import List

from nose.tools import assert_list_equal


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {c: i for i, c in enumerate(s)}
        j = anchor = 0
        ans = []

        for i, c in enumerate(s):
            j = max(j, last[c])
            if i == j:
                ans.append(i - anchor + 1)
                anchor = i + 1
        return ans


class testSuits:

    @staticmethod
    def test(sol):
        assert_list_equal(sol("ababcbacadefegdehijhklij"), [9, 7, 8])
        assert_list_equal(sol("eccbbbbdec"), [10])
        print('ALL TEST CASES PASSED')


solObj = Solution()
t = testSuits()
t.test(solObj.partitionLabels)
