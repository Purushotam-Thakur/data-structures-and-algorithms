from nose.tools import assert_true, assert_false


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket = {')': '(', ']': '[', '}': '{'}

        for i in s:
            if i in bracket.values():
                stack.append(i)
            elif i in bracket.keys():
                if stack == [] or stack.pop() != bracket[i]:
                    return False
            else:
                return False
        return stack == []


class testSuits:

    @staticmethod
    def test(sol):
        assert_true(sol('()'))
        assert_true(sol("()[]{}"))
        assert_false(sol("(]"))
        print('ALL TEST CASES PASSED')


s = Solution()
t = testSuits()
t.test(s.isValid)
