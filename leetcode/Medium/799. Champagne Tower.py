class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        track = [[0] * k for k in range(1, 102)]
        track[0][0] = poured

        for r in range(query_row + 1):
            for c in range(r + 1):
                q = (track[r][c] - 1.0) / 2.0
                if q > 0:
                    track[r + 1][c] += q
                    track[r + 1][c + 1] += q
        return min(1, track[query_row][query_glass])