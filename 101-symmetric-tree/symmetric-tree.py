# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if root == None:
            return True
        
        return self.areMirrored(root.left, root.right)
    
    def areMirrored(self, left, right):

        # handle one or both left and right None
        if left == None and right == None:
            return True
        if left == None or right == None:
            return False
        
        # handle left and right val not equals
        if left.val != right.val:
            return False
        
        # check children mirrored
        return self.areMirrored(left.left, right.right) and self.areMirrored(left.right, right.left)

        