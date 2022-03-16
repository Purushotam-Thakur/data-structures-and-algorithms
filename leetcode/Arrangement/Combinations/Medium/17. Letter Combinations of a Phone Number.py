from typing import List
from nose.tools import assert_equal


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return list(phone[digits[0]])

        prev = self.letterCombinations(digits[:-1])
        current = phone[digits[-1]]
        return [p + c for p in prev for c in current]


class letterCombinationsTest:

    @staticmethod
    def test(sol):
        assert_equal(sol('23'), ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
        assert_equal(sol(''), [])
        assert_equal(sol('2'), ["a", "b", "c"])
        print('ALL TEST CASES PASSED')


s = Solution()
t = letterCombinationsTest()
t.test(s.letterCombinations)
