class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # handle base cases len(nums) <= 2
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            if nums[0] > nums[1]:
                return nums[1]
            else:
                return nums[0]

        # binary search
        mid = int(len(nums) / 2)
        lo = 0
        hi = len(nums) - 1
        if nums[mid] > nums[hi]:
            return self.findMin(nums[mid:])
        return self.findMin(nums[:mid + 1])

        
        