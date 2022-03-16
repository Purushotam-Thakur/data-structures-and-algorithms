from typing import List

from nose.tools import assert_true, assert_false


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        track = {}
        for i, s in enumerate(order):
            track[s] = i

        for i in range(len(words) - 1):
            for j in range(len(words[i])):
                if j >= len(words[i + 1]):
                    return False
                if words[i][j] != words[i + 1][j]:
                    if track[words[i][j]] > track[words[i + 1][j]]:
                        return False
                    break
        return True


class testSuits:

    @staticmethod
    def test(sol):
        assert_true(sol(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))
        assert_false(sol(["word", "world", "row"], "worldabcefghijkmnpqstuvxyz"))
        print('ALL TEST CASES PASSED')


solObj = Solution()
t = testSuits()
t.test(solObj.isAlienSorted)
