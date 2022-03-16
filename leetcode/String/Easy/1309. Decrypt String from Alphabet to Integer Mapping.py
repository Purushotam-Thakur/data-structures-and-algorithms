from nose.tools import assert_equal


class Solution:
    def freqAlphabets(self, s: str) -> str:
        for i in range(26, 0, -1):
            s = s.replace(str(i) + '#' * (i > 9), chr(96 + i))
        return s


class testSuits:

    @staticmethod
    def test(sol):
        assert_equal(sol("10#11#12"), "jkab")
        assert_equal(sol("1326#"), "acz")
        print('ALL TEST CASES PASSED')


solObj = Solution()
t = testSuits()
t.test(solObj.freqAlphabets)
