from typing import List

from nose.tools import assert_true, assert_false


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        track = [False] * len(rooms)
        track[0] = True

        stack = [0]
        while stack:
            key = stack.pop()
            for i in rooms[key]:
                if not track[i]:
                    track[i] = True
                    stack.append(i)

        return all(track)


class testSuits:

    @staticmethod
    def test(sol):
        assert_true(sol([[1], [2], [3], []]))
        assert_false(sol([[1, 3], [3, 0, 1], [2], [0]]))
        print('ALL TEST CASES PASSED')


solObj = Solution()
t = testSuits()
t.test(solObj.canVisitAllRooms)
