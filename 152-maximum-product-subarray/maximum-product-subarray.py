class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = nums[0]
        s = nums[0]
        m = nums[0]
        for i in range(1, len(nums)):
            l_new = max(l * nums[i], s * nums[i], nums[i])
            s_new = min(l * nums[i], s * nums[i], nums[i])
            l = l_new
            s = s_new
            if l > m:
                m = l
        return m

        