class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L = [nums[0]]
        S = [nums[0]]
        for i in range(1, len(nums)):
            l = max([L[i-1] * nums[i], S[i-1] * nums[i], nums[i]])
            L.append(l)
            s = min([L[i-1] * nums[i], S[i-1] * nums[i], nums[i]])
            S.append(s)
        return max(L)
        