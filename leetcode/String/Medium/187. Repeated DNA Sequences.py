import collections
from typing import List

from nose.tools import assert_list_equal


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        track = collections.defaultdict(int)

        for i in range(len(s)):
            track[s[i:i + 10]] += 1

        return [key for key, value in track.items() if value > 1]


class testSuits:

    @staticmethod
    def test(sol):
        assert_list_equal(sol("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"), ["AAAAACCCCC", "CCCCCAAAAA"])
        assert_list_equal(sol("AAAAAAAAAAAAA"), ["AAAAAAAAAA"])
        print('ALL TEST CASES PASSED')


solObj = Solution()
t = testSuits()
t.test(solObj.findRepeatedDnaSequences)
