from typing import List
from nose.tools import assert_equal


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        pal = longest_pal = 0
        count = {n: 0 for n in words}
        print(count)

        for st in words:
            if st[0] == st[1]:
                if count[st] > 0:
                    longest_pal += 4
                    pal -= 1
                    count[st] -= 1
                else:
                    count[st] += 1
                    pal += 1
            else:
                if st[::-1] in count and count[st[::-1]] > 0:
                    longest_pal += 4
                    count[st[::-1]] -= 1
                else:
                    count[st] += 1

        return longest_pal + 2 if pal > 0 else longest_pal


class longest_palindrome_test:

    @staticmethod
    def test(sol):
        assert_equal(sol(["dd", "aa", "bb", "dd", "aa", "dd", "bb", "dd", "aa", "cc", "bb", "cc", "dd", "cc"]), 22)
        assert_equal(sol(["lc", "cl", "gg"]), 6)
        assert_equal(sol(["ab", "ty", "yt", "lc", "cl", "ab"]), 8)
        assert_equal(sol(["cc", "ll", "xx"]), 2)
        print('ALL TEST CASES PASSED')


t = longest_palindrome_test()
s = Solution()
t.test(s.longestPalindrome)
