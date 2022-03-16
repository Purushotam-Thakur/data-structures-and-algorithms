from nose.tools import assert_false, assert_true


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        track_s = {}
        track_p = {}
        s = s.split(' ')

        if len(s) != len(pattern):
            return False

        for i in range(len(pattern)):
            if (s[i] in track_s and track_s[s[i]] != pattern[i]) or (
                    pattern[i] in track_p and track_p[pattern[i]] != s[i]):
                return False
            track_s[s[i]] = pattern[i]
            track_p[pattern[i]] = s[i]
        return True


class testSuits:

    @staticmethod
    def test(sol):
        assert_true(sol("abba", "dog cat cat dog"))
        assert_false(sol("abba", "dog cat cat fish"))
        assert_false(sol("aaaa", "dog cat cat dog"))
        print('ALL TEST CASES PASSED')


solObj = Solution()
t = testSuits()
t.test(solObj.addStrings)