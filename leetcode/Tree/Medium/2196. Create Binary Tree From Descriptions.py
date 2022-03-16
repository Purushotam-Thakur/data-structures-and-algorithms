# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        track = {}
        for i in descriptions:
            if i[1] in track:
                track[i[1]][1] = False
            else:
                track[i[1]] = [TreeNode(i[1]), False]
            if i[0] in track:
                if i[2] == 1:
                    track[i[0]][0].left = TreeNode(i[1])
                else:
                    track[i[0]][0].right = TreeNode(i[1])
            else:
                child = TreeNode(i[1])
                parent = TreeNode(i[0])
                if i[2] == 1:
                    parent.left = child
                else:
                    parent.right = child
                track[i[0]] = [parent, True]
        root = None
        ans = None
        for i in track:
            if track[i][1]:
                root = track[i][0]
                ans = track[i][0]

        def prepareTree(root):
            if root.left:
                root.left = track[root.left.val][0]
                prepareTree(root.left)
            if root.right:
                root.right = track[root.right.val][0]
                prepareTree(root.right)

        prepareTree(root)
        return ans


class Solution1:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        children = set()
        m = {}
        for p, c, l in descriptions:
            np = m.setdefault(p, TreeNode(p))
            nc = m.setdefault(c, TreeNode(c))
            if l:
                np.left = nc
            else:
                np.right = nc
            children.add(c)
        root = (set(m) - set(children)).pop()
        return m[root]
