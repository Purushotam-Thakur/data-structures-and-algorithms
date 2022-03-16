from typing import List
from nose.tools import assert_list_equal


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(S, left, right):
            if len(S) == 2 * n:
                ans.append("".join(S))
                return
            if left < n:
                S.append("(")
                backtrack(S, left + 1, right)
                S.pop()
            if right < left:
                S.append(")")
                backtrack(S, left, right + 1)
                S.pop()

        backtrack([], 0, 0)
        return ans


class testSuits:

    @staticmethod
    def test(sol):
        assert_list_equal(sol(3), ["((()))", "(()())", "(())()", "()(())", "()()()"])
        assert_list_equal(sol(1), ["()"])
        print('ALL TEST CASES PASSED')


s = Solution()
t = testSuits()
t.test(s.generateParenthesis)
