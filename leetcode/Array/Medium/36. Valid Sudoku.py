from typing import List

from nose.tools import assert_true, assert_false


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        track = set()

        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    val = board[r][c]
                    if (r, val) in track or (val, c) in track or (r // 3, c // 3, val) in track:
                        return False
                    track.add((r, val))
                    track.add((val, c))
                    track.add((r // 3, c // 3, val))
        return True


class testSuits:

    @staticmethod
    def test(sol):
        assert_true(sol([["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                         [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                         ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                         [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
        assert_false(sol([["8", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                          [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                          ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                          [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                          [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
        print('ALL TEST CASES PASSED')


s = Solution()
t = testSuits()
t.test(s.isValidSudoku)
