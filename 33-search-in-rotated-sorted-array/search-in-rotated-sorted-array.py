class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            if target == nums[0]:
                return 0
            else:
                return -1
        
        # set up lo, mid, hi indices
        mid = int(len(nums) / 2)
        lo = 0
        hi = len(nums) - 1

        # if mid is solution, return its index
        if nums[mid] == target:
            return mid

        # else determine which of left and right is in correct order
        if nums[lo] < nums[mid]:
            # left is in correct order
            if nums[lo] <= target and target <= nums[mid]:
                # target is within left interval
                return self.search(nums[:mid], target)
            else:
                # target is within right interval
                right_res = self.search(nums[mid + 1:], target)
                if right_res == -1:
                    return -1
                else:
                    return right_res + mid + 1
        else:
            # right is in correct order
            if nums[mid] <= target and target <= nums[hi]:
                # target is within right interval
                right_res = self.search(nums[mid + 1:], target)
                if right_res == -1:
                    return -1
                else:
                    return right_res + mid + 1
            else:
                # target is within left interval
                return self.search(nums[:mid], target)

        return 0
        
        