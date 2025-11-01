# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """

        # handle special case
        if nums == []:
            return None

        # compute mid, make root node
        mid = int(len(nums) / 2)
        root = TreeNode(nums[mid])

        # get left tree
        root.left = self.sortedArrayToBST(nums[:mid])

        # get right tree
        root.right = self.sortedArrayToBST(nums[mid + 1:])

        return root
        