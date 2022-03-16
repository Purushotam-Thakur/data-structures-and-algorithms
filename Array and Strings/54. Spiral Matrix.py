from typing import List


class Solution:
    def spiral_order(self, matrix: List[List[int]]) -> List[int]:
        return matrix and [*matrix.pop(0)] + self.spiral_order([*zip(*matrix)][::-1])


matrix_input = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
run = Solution()
res = run.spiral_order(matrix_input)
print(res)
