from nose.tools import assert_equal


class Solution:
    def simplifyPath(self, path: str) -> str:
        places = [f for f in path.split('/') if f != '.' and f != '']
        stack = []
        for f in places:
            if f == '..':
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(f)

        return '/' + '/'.join(stack)


class testSuits:

    @staticmethod
    def test(sol):
        assert_equal(sol('/home/'), '/home')
        assert_equal(sol('/..'), '/')
        assert_equal(sol('/home//foo/'), '/home//foo/')
        assert_equal(sol('/home/../hello//test//'), '/hello/test')
        print('ALL TEST CASES PASSED')


s = Solution()
t = testSuits()
t.test(s.simplifyPath)
