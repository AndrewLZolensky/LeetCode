# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """

        if root == None:
            return False
        if root.left == None and root.right == None:
            return targetSum == root.val
        if root.left == None:
            return self.hasPathSum(root.right, targetSum - root.val)
        if root.right == None:
            return self.hasPathSum(root.left, targetSum - root.val)

        hasPathLeft = self.hasPathSum(root.left, targetSum - root.val)
        hasPathRight = self.hasPathSum(root.right, targetSum - root.val)

        return hasPathLeft or hasPathRight
        