from collections import Counter

from nose.tools import assert_equal


class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = Counter(s)
        print(cnt)
        s = list(s)
        print(s)
        s.sort(key=lambda x:(-cnt[x], x))
        return "".join(s)


class testSuits:

    @staticmethod
    def test(sol):
        assert_equal(sol("tree"), "eert")
        assert_equal(sol("cccaaa"), "aaaccc")
        assert_equal(sol("Aacbcbc"), "cccbbAa")
        print('ALL TEST CASES PASSED')


solObj = Solution()
t = testSuits()
t.test(solObj.frequencySort)
