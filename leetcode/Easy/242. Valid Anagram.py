import collections

from nose.tools import assert_true, assert_false


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return not collections.Counter(s) - collections.Counter(t)


    def isAnagram1(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        track = {}
        for i in s:
            if i in track:
                track[i] += 1
            else:
                track[i] = 1

        for i in t:
            if i not in track or track[i] < 1:
                return False
            track[i] -= 1
        return True


class testSuits:

    @staticmethod
    def test(sol):
        assert_true(sol("anagram", "nagaram"))
        assert_false(sol("rat", "cat"))
        print('ALL TEST CASES PASSED')


s = Solution()
t = testSuits()
t.test(s.isAnagram)
t.test(s.isAnagram1)
