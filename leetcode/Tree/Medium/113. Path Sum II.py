from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        self.dfs(root, targetSum, [], res)
        return res

    def dfs(self, root, total, track, res):
        if root:
            if not root.left and not root.right and root.val == total:
                track.append(root.val)
                res.append(track)

            self.dfs(root.left, total - root.val, track + [root.val], res)
            self.dfs(root.right, total - root.val, track + [root.val], res)
