import collections
from typing import List

from nose.tools import assert_list_equal


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        track = collections.defaultdict(list)

        for i in strs:
            track[''.join(sorted(i))].append(i)
        return track.values()


class testSuits:

    @staticmethod
    def test(sol):
        assert_list_equal(sol(["eat", "tea", "tan", "ate", "nat", "bat"]),
                          [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]])
        assert_list_equal(sol([""]), [[""]])
        assert_list_equal(sol(["a"]), [["a"]])
        print('ALL TEST CASES PASSED')


solObj = Solution()
t = testSuits()
t.test(solObj.groupAnagrams)
