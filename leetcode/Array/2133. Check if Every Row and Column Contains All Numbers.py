from typing import List


class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)

        for i in range(n):
            check_r = [0] * n
            check_c = [0] * n
            for j in range(n):
                r_v = matrix[i][j] - 1
                c_v = matrix[j][i] - 1

                if check_r[r_v] != 0 or check_c[c_v] != 0:
                    return False
                else:
                    check_r[r_v] = -1
                    check_c[c_v] = -1

        return True


s = Solution()
print(s.checkValid([[1, 2, 3], [3, 1, 2], [2, 3, 1]]))
