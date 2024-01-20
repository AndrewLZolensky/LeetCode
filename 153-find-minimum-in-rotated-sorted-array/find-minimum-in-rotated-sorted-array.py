class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        while start < end:
            middle = (end + start) // 2
            if (nums[middle] > nums[end]):
                start = middle + 1
            else:
                end = middle
        return nums[start]     