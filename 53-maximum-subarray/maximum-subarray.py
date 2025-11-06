class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]
        curr_sum = 0
        lo = 0
        hi = 0
        while hi < len(nums):

            # increment current sum by number at hi
            curr_sum += nums[hi]

            # check if current sum is larger than previous max
            if curr_sum > max_sum:
                max_sum = curr_sum

            # incremement hi
            hi += 1

            # if curr sum is negative, clear it and move lo to hi
            if curr_sum < 0:
                lo = hi
                curr_sum = 0
        
        return max_sum