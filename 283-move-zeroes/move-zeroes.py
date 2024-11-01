class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        r = 0
        w = 0
        while (r < len(nums)):
            if (nums[w] == 0) and (nums[r] != 0):
                hold = nums[w]
                nums[w] = nums[r]
                nums[r] = hold
                w += 1
            elif (nums[w] == 0) and (nums[r] == 0):
                pass
            elif (nums[w] != 0):
                w += 1
            r += 1
        