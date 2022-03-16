from typing import List

from nose.tools import assert_true, assert_false


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i = 0
        l = len(popped)

        for n in pushed:
            stack.append(n)
            while stack and i < l and popped[i] == stack[-1]:
                stack.pop()
                i += 1
        return i == l


class testSuits:

    @staticmethod
    def test(sol):
        assert_true(sol([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))
        assert_false(sol([1, 2, 3, 4, 5], [4, 5, 3, 1, 2]))
        print('ALL TEST CASES PASSED')


solObj = Solution()
t = testSuits()
t.test(solObj.validateStackSequences)
