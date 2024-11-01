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
        count = 1
        if root.left:
            count += self.countNodes(root.left)
        if root.right:
            count += self.countNodes(root.right)
        return count