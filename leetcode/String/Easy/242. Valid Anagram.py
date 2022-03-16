from nose.tools import assert_true, assert_false


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


class testSuits:

    @staticmethod
    def test(sol):
        assert_true(sol("anagram", "nagaram"))
        assert_false(sol("rat#", "car"))
        print('ALL TEST CASES PASSED')


solObj = Solution()
t = testSuits()
t.test(solObj.isAnagram)
