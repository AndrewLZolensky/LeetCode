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
            if nums[low] == nums[high]: # if we have singleton, return index to left or right
                if target > nums[high]:
                    return high + 1
                else:
                    return low
            if nums[mid] > target:
                high = mid - 1
            if nums[mid] < target:
                low = mid + 1
        
        return low
        
        