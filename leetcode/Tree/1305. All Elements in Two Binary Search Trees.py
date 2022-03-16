from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def inOrder(root, result):
            if not root:
                return
            inOrder(root.left, result)
            result.append(root.val)
            inOrder(root.right, result)

        res = []
        inOrder(root1, res)
        inOrder(root2, res)

        return sorted(res)

    def getAllElements1(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def inOrder(root, result):
            if not root:
                return
            inOrder(root.left, result)
            result.append(root.val)
            inOrder(root.right, result)

        list1 = []
        list2 = []
        inOrder(root1, list1)
        inOrder(root2, list2)

        n = len(list1)
        m = len(list2)
        i = j = 0

        res = []
        while i < n and j < m:
            if list1[i] < list2[j]:
                res.append(list1[i])
                i += 1
            else:
                res.append(list2[j])
                j += 1

        if i < n:
            res = res + list1[i:]
        if j < m:
            res = res + list2[j:]
        return res

