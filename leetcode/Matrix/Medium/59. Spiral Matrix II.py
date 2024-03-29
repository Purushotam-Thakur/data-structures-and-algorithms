class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if not n:
            return []
        left, right, top, down = 0, n - 1, 0, n - 1
        count = 1
        res = [[0 for _ in range(n)] for _ in range(n)]
        while left <= right and top <= down:
            for i in range(left, right + 1):
                res[top][i] = count
                count += 1
            top += 1
            for i in range(top, down + 1):
                res[i][right] = count
                count += 1
            right -= 1

            for i in range(right, left - 1, -1):
                res[down][i] = count
                count += 1
            down -= 1

            for i in range(down, top - 1, -1):
                res[i][left] = count
                count += 1
            left += 1
        return res
