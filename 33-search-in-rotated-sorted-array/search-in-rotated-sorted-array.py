class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        while (start <= end):

            middle = (start + end) // 2

            if (nums[middle] == target):
                return middle
            
            if (nums[start] <= nums[middle]):
                if (nums[start] <= target) and (target < nums[middle]):
                    end = middle - 1
                else:
                    start = middle + 1
            else:
                if (nums[middle] < target) and (target <= nums[end]):
                    start = middle + 1
                else:
                    end = middle - 1
        
        return -1

        