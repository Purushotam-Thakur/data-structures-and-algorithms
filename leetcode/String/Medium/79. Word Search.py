from typing import List
from nose.tools import assert_true, assert_false


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False

    def dfs(self, board, i, j, word) -> bool:
        if len(word) == 0:
            return True

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:
            return False

        temp = board[i][j]
        board[i][j] = '#'

        res = self.dfs(board, i - 1, j, word[1:]) \
              or self.dfs(board, i + 1, j, word[1:]) \
              or self.dfs(board, i, j - 1, word[1:]) \
              or self.dfs(board, i, j + 1, word[1:])

        board[i][j] = temp
        return res


class testSuits:

    @staticmethod
    def test(sol):
        assert_true(sol([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"))
        assert_true(sol([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"))
        assert_true(sol([["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]], "AAB"))
        assert_false(sol([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"))
        print('ALL TEST CASES PASSED')


s = Solution()
t = testSuits()
t.test(s.exist)
