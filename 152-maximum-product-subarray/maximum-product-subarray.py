class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minprod = maxprod = ans = nums[0]
        for n in nums[1:]:
            min_temp = minprod*n
            max_temp = maxprod*n
            maxprod = max(min_temp, max_temp, n)
            minprod = min(min_temp, max_temp, n)
            ans = max(ans, maxprod)
        return ans
        