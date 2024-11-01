from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        flat_p = self.bfs(p)
        flat_q = self.bfs(q)
        if (len(flat_p) != len(flat_q)):
            return False
        for i in range(len(flat_p)):
            if (flat_p[i] != flat_q[i]):
                return False
        return True
    
    def bfs(self, n):
        flattened = list()
        queue = deque()
        queue.append(n)
        while (len(queue) > 0):
            curr = queue.popleft()
            if (curr == None):
                flattened.append(curr)
            else:
                flattened.append(curr.val)
                queue.append(curr.left)
                queue.append(curr.right)
        return flattened
        