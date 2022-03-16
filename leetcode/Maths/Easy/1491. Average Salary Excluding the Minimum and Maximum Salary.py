from typing import List

from nose.tools import assert_equal


class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        n = len(salary)

        return sum(salary[1:n - 1]) / (n - 2)


class testSuits:

    @staticmethod
    def test(sol):
        assert_equal(sol([4000, 3000, 1000, 2000]), 2500.00000)
        assert_equal(sol([1000, 2000, 3000]), 2000.00000)
        print('ALL TEST CASES PASSED')


s = Solution()
t = testSuits()
t.test(s.average)
