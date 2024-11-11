class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        values = []
        for i in range(len(nums)):
            if i == 0:
                values.append(nums[i])
            elif i == 1:
                values.append(max(nums[i-1], nums[i]))
            else:
                values.append(max(values[i-2] + nums[i], values[i-1]))
        
        return values[-1]
        