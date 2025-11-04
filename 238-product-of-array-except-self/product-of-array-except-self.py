class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prods = [1]
        for i in range(len(nums) - 1):
            prods.append(nums[i] * prods[-1])
        multiplier = 1
        for i in range(1, len(nums) + 1):
            prods[-i] *= multiplier
            multiplier *= nums[-i]
        return prods

        