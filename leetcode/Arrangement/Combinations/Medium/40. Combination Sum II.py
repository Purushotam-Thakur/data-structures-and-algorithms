from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(pos, current, target):
            if 0 == target:
                res.append(current.copy())
                return
            if target < 0:
                return
            prev = -1
            for i in range(pos, len(candidates)):
                if candidates[i] == prev:
                    continue
                current.append(candidates[i])
                backtrack(i + 1, current, target - candidates[i])
                current.pop()
                prev = candidates[i]

        backtrack(0, [], target)
        return res

