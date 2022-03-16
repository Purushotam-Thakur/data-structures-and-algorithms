import string
from typing import List

from nose.tools import assert_list_equal


class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        c1, c2, r1, r2 = ord(s[0]), ord(s[3]), int(s[1]), int(s[4])
        return [chr(c) + str(r) for c in range(c1, c2 + 1) for r in range(r1, r2 + 1)]


class Solution1:
    def cellsInRange(self, s: str) -> List[str]:
        alphabet = string.ascii_uppercase
        a_l = list(alphabet)
        ans = []
        range_s = s.split(':')
        start_c = a_l.index(range_s[0][0])
        end_c = a_l.index(range_s[1][0])
        start_r = int(range_s[0][1])
        end_r = int(range_s[1][1])

        for c in range(start_c, end_c + 1):
            for r in range(start_r, end_r + 1):
                ans.append(a_l[c] + (str(r)))

        return ans


class testSuits:

    @staticmethod
    def test(sol):
        assert_list_equal(sol("K1:L2"), ["K1", "K2", "L1", "L2"])
        assert_list_equal(sol("A1:F1"), ["A1", "B1", "C1", "D1", "E1", "F1"])
        print('ALL TEST CASES PASSED')


s = Solution()
s1 = Solution1()
t = testSuits()
t.test(s.cellsInRange)
t.test(s1.cellsInRange)
