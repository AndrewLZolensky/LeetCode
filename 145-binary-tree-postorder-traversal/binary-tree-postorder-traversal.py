# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if root == None:
            return []
        traversal = self.postorderTraversal(root.left)
        traversal.extend(self.postorderTraversal(root.right))
        traversal.append(root.val)
        return traversal
        