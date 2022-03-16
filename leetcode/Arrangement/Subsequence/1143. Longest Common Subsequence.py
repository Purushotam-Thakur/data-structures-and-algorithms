from nose.tools import assert_equal


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        # use the equations from the recursion
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        return dp[-1][-1]


class testSuits:

    @staticmethod
    def test(sol):
        assert_equal(sol("abcde", "ace"), 3)
        assert_equal(sol("abc", "abc"), 3)
        assert_equal(sol("abc", "def"), 0)
        print('ALL TEST CASES PASSED')


s = Solution()
t = testSuits()
t.test(s.longestCommonSubsequence)
