# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1
        if root.left == None:
            return self.minDepth(root.right) + 1
        if root.right == None:
            return self.minDepth(root.left) + 1
        
        min_depth_left = self.minDepth(root.left) + 1
        min_depth_right = self.minDepth(root.right) + 1

        if min_depth_right < min_depth_left:
            return min_depth_right

        return min_depth_left
        