class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        for i in range(len(nums) + 1):
            total += i
        for el in nums:
            total -= el
        return total
        