from nose.tools import assert_equal


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'

        m, n = len(num1), len(num2)
        res = [0] * (m + n)

        num1_rev = num1[::-1]
        num2_rev = num2[::-1]

        for i2, v2 in enumerate(num2_rev):
            for i1, v1 in enumerate(num1_rev):
                num_0 = i1 + i2

                carry = res[num_0]
                multiplication = int(v1) * int(v2) + carry
                res[num_0] = multiplication % 10
                res[num_0 + 1] += multiplication // 10
        if res[-1] == 0:
            res.pop()

        return ''.join(str(v) for v in reversed(res))


class testSuits:

    @staticmethod
    def test(sol):
        assert_equal(sol("2", "3"), "6")
        assert_equal(sol("123", "456"), "56088")
        print('ALL TEST CASES PASSED')


solObj = Solution()
t = testSuits()
t.test(solObj.multiply)
