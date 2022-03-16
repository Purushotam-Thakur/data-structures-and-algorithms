from nose.tools import assert_equal


class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        for i in range(len(s)):
            temp = self.helper(i, i, s)
            if len(temp) > len(res):
                res = temp
            temp = self.helper(i, i + 1, s)

            if len(temp) > len(res):
                res = temp
        return res

    def helper(self, l, r, s):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r]


class testSuits:

    @staticmethod
    def test(sol):
        assert_equal(sol("babad"), "bab")
        assert_equal(sol("cbbd"), "bb")
        print('ALL TEST CASES PASSED')


solObj = Solution()
t = testSuits()
t.test(solObj.longestPalindrome)
