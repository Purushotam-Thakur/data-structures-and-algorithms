from nose.tools import assert_equal


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y, dx, dy = 0, 0, 0, 1

        for i in instructions:
            if i == 'R':
                dx, dy = dy, -dx
            if i == 'L':
                dx, dy = -dy, dx
            if i == 'G':
                x, y = x + dx, y + dy
        return (x, y) == (0, 0) or (dx, dy) != (0, 1)


class isRobotBoundedTest:

    @staticmethod
    def test(sol):
        assert_equal(sol('GGLLGG'), True)
        assert_equal(sol('GG'), False)
        assert_equal(sol('GL'), True)
        print('ALL TEST CASES PASSED')


s = Solution()
t = isRobotBoundedTest()
t.test(s.isRobotBounded)
