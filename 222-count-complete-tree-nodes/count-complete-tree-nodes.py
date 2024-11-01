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
        # do dfs
        # add 1 for each child
        if root == None:
            return 0
        return self.dfs(root)
    
    def dfs(self, node):
        count = 1
        if node.left:
            count += self.dfs(node.left)
        if node.right:
            count += self.dfs(node.right)
        return count