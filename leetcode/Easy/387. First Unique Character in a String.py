from nose.tools import assert_equal


class Solution:
    def firstUniqChar(self, s: str) -> int:
        n = len(s)
        res = n + 1
        track = {}
        for i in s:
            if i in track:
                track[i] += 1
            else:
                track[i] = 1

        for i in range(n):
            if track[s[i]] == 1:
                return i
        return -1


class testSuits:

    @staticmethod
    def test(sol):
        assert_equal(sol("leetcode"), 0)
        assert_equal(sol("loveleetcode"), 2)
        assert_equal(sol("loveleetcodev"), 7)
        assert_equal(sol("loveleetcodevt"), 8)
        assert_equal(sol("loveleetcodevtcd"), -1)
        print('ALL TEST CASES PASSED')


s = Solution()
t = testSuits()
t.test(s.firstUniqChar)
