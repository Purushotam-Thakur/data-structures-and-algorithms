from typing import List

from nose.tools import assert_equal


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        count = [0] * (n + 1)

        for a, b in trust:
            count[a] -= 1
            count[b] += 1

        for i in range(1, n + 1):
            if count[i] == n - 1:
                return i

        return -1


class Solution1:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        judge = dict.fromkeys(range(1, n + 1), 0)
        people = dict.fromkeys(range(1, n + 1), 0)

        if len(trust) < 1 and n > 1:
            return -1

        if len(trust) < 1:
            return 1

        for i in trust:
            people[i[1]] += 1
            if judge[i[1]] != -1:
                judge[i[1]] = 1
            if i[0] in judge:
                judge[i[0]] = -1

        for i in range(1, n + 1):
            if judge[i] == 1 and people[i] == n - 1:
                return i

        return -1


class testSuits:

    @staticmethod
    def test(sol):
        assert_equal(sol(2, [[1, 2]]), 2)
        assert_equal(sol(3, [[1, 3], [2, 3]]), 3)
        assert_equal(sol(3, [[1, 3], [2, 3], [3, 1]]), -1)
        print('ALL TEST CASES PASSED')


solObj = Solution()
solObj1 = Solution1()
t = testSuits()
t.test(solObj.findJudge)
t.test(solObj1.findJudge)
