# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root == None:
            return 0
        max_left = self.maxDepth(root.left) + 1
        max_right = self.maxDepth(root.right) + 1
        if max_left > max_right:
            return max_left
        return max_right
        