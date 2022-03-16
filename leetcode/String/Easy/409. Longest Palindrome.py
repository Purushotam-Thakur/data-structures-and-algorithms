import collections

from nose.tools import assert_equal


class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans = 0
        for count in collections.Counter(s).values():
            ans += count // 2 * 2
            if ans % 2 == 0 and count % 2 == 1:
                ans += 1
        return ans


class testSuits:

    @staticmethod
    def test(sol):
        assert_equal(sol("abccccdd"), 7)
        assert_equal(sol("ab"), 1)
        assert_equal(sol("abb"), 3)
        print('ALL TEST CASES PASSED')


solObj = Solution()
t = testSuits()
t.test(solObj.longestPalindrome)
