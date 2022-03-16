from nose.tools import assert_true, assert_false


class Solution:
    def isHappy(self, n: int) -> bool:
        track = []
        while n not in track and n != 1:
            track.append(n)
            n = self.square_sum(n)
        return n == 1

    def square_sum(self, num):
        total = 0
        while num > 9:
            r = num % 10
            num = num // 10
            total += r * r
        total += num * num
        return total


class testSuits:

    @staticmethod
    def test(sol):
        assert_true(sol(19))
        assert_false(sol(2))
        print('ALL TEST CASES PASSED')


s = Solution()
t = testSuits()
t.test(s.isHappy)
