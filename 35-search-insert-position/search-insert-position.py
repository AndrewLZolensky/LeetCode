class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        low = 0
        high = n - 1
        while low <= high:
            mid = (low + high) // 2 # calculate mid
            if nums[mid] == target: # if we found target, return index
                return mid
            if nums[mid] > target: # otherwise recurse on correct side
                high = mid - 1
            if nums[mid] < target:
                low = mid + 1
        
        return low 
        
        