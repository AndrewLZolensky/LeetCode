class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxsum = float('-inf')
        curr = 0
        
        for num in nums:
            if curr >= 0:
                curr += num
            else:
                curr = num
            if curr > maxsum:
                maxsum = curr
        
        return(maxsum)