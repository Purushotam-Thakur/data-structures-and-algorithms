# Definition for a Node.
# https://leetcode.com/problems/clone-graph/discuss/42314/Python-solutions-(BFS-DFS-iteratively-DFS-recursively).

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        new_node = {node: Node(node.val)}
        stack = [node]
        while stack:
            curr_node = stack.pop()
            for n in curr_node.neighbors:
                if n not in new_node:
                    stack.append(n)
                    new_node[n] = Node(n.val)
                new_node[curr_node].neighbors.append(new_node[n])
        return new_node[node]

    def cloneGraph2(self, node):  # BFS
        if not node:
            return node
        m = {node: Node(node.val)}
        deque = collections.deque([node])
        while deque:
            n = deque.popleft()
            for neigh in n.neighbors:
                if neigh not in m:
                    deque.append(neigh)
                    m[neigh] = Node(neigh.val)
                m[n].neighbors.append(m[neigh])
        return m[node]

    def cloneGraph3(self, node):  # DFS recursively
        if not node:
            return node
        m = {node: Node(node.val)}
        self.dfs(node, m)
        return m[node]

    def dfs(self, node, m):
        for neigh in node.neighbors:
            if neigh not in m:
                m[neigh] = Node(neigh.val)
                self.dfs(neigh, m)
            m[node].neighbors.append(m[neigh])
