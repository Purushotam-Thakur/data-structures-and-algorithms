from typing import List

from nose.tools import assert_equal


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []

        for i in range(1, 9):
            track = count = i

            while track <= high and count < 10:
                if track >= low:
                    res.append(track)
                count += 1
                track = track * 10 + count
        return sorted(res)


class testSuits:

    @staticmethod
    def test(sol):
        assert_equal(sol(100, 300), [123, 234])
        assert_equal(sol(1000, 13000), [1234, 2345, 3456, 4567, 5678, 6789, 12345])
        assert_equal(sol(58, 155), [67, 78, 89, 123])
        print('ALL TEST CASES PASSED')


s = Solution()
t = testSuits()
t.test(s.sequentialDigits)
