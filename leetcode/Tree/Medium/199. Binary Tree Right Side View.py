# Definition for a binary tree node.
import collections
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class SolutionTest:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        stack = [[root]]
        res = []

        while len(stack) > 0:
            track = stack.pop()
            new_list = []
            res.append(track[-1].val)

            for node in track:
                if node.left:
                    new_list.append(node.left)
                if node.right:
                    new_list.append(node.right)
            if len(new_list) > 0:
                stack.append(new_list)
        return res


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = collections.deque()

        if root:
            queue.append(root)

        res = []

        while queue:
            size, val = len(queue), 0

            for _ in range(size):
                node = queue.popleft()
                val = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(val)
        return res
