class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        top = 0
        bottom = 0
        prev = -(nums[0]+1)
        while (top < len(nums)):
            if (nums[top] != prev):
                nums[bottom] = nums[top]
                bottom += 1
            top += 1
            prev = nums[top - 1]
        return bottom
        