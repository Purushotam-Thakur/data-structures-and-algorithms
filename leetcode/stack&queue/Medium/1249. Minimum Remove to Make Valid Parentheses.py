from nose.tools import assert_equal


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        stack = []

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    s[i] = ''
        while stack:
            s[stack.pop()] = ''
        return ''.join(s)


class testSuits:

    @staticmethod
    def test(sol):
        assert_equal(sol("lee(t(c)o)de)"), "lee(t(c)o)de")
        assert_equal(sol("a)b(c)d"), "ab(c)d")
        assert_equal(sol("))(("), "")
        print('ALL TEST CASES PASSED')


solObj = Solution()
t = testSuits()
t.test(solObj.minRemoveToMakeValid)
