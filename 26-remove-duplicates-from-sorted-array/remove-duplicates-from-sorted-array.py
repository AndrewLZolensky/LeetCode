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
            if (nums[top] == prev):
                top += 1
            else:
                nums[bottom] = nums[top]
                top += 1
                bottom += 1
            prev = nums[top - 1]
        return bottom
        