class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # m[i] = max we can rob while stopping at or before house i
        # m[i] = max(m[i-1], m[i-2] + nums[i - 1])

        # base case
        if len(nums) == 0:
            return 0
        
        # recursion
        m = [0, nums[0]]
        for i in range(2, len(nums) + 1):
            m.append(max(m[i - 1], m[i - 2] + nums[i - 1]))

        # max
        return max(m)
        
        

        