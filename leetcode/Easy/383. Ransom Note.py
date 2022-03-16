import collections

from nose.tools import assert_true, assert_false


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return not collections.Counter(ransomNote) - collections.Counter(magazine)


    def canConstruct2(self, ransomNote: str, magazine: str) -> bool:
        track = {}

        for i in magazine:
            if i in track:
                track[i] += 1
            else:
                track[i] = 1
        for i in ransomNote:
            if i in track and track[i] > 0:
                track[i] -= 1
            else:
                return False
        return True


    def canConstruct1(self, ransomNote: str, magazine: str) -> bool:
        for i in ransomNote:
            if ransomNote.count(i) > magazine.count(i):
                return False
        return True



class testSuits:

    @staticmethod
    def test(sol):
        assert_true(sol("aa", "aba"))
        assert_false(sol("aa", "ab"))
        print('ALL TEST CASES PASSED')


s = Solution()
t = testSuits()
t.test(s.canConstruct)
t.test(s.canConstruct1)
t.test(s.canConstruct2)
