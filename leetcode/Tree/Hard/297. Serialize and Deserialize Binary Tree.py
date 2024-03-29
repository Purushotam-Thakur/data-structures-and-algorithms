# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def inOrder(node):
            if node:
                vals.append(str(node.val))
                inOrder(node.left)
                inOrder(node.right)
            else:
                vals.append('#')

        vals = []
        inOrder(root)
        return ' '.join(vals)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def buildTree():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = buildTree()
            node.right = buildTree()
            return node

        vals = iter(data.split())
        return buildTree()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
