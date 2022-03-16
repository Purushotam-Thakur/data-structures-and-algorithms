from nose.tools import assert_equal


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        def str_to_int(num):
            res = 0
            for i in num:
                res = res * 10 + ord(i) - ord('0')
            return res

        return str(str_to_int(num1) + str_to_int(num2))


class testSuits:

    @staticmethod
    def test(sol):
        assert_equal(sol("11", "123"), "134")
        assert_equal(sol("456", "77"), "533")
        assert_equal(sol("0", "0"), "0")
        print('ALL TEST CASES PASSED')


solObj = Solution()
t = testSuits()
t.test(solObj.addStrings)
