from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # do bfs
        # add 1 for each child
        if root == None:
            return 0
        count = 0
        q = deque()
        q.append(root)
        while (len(q) > 0):
            curr = q.popleft()
            count += 1
            if (curr.left != None):
                q.append(curr.left)
            if (curr.right != None):
                q.append(curr.right)
        return count
        