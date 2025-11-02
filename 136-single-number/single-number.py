class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = 0
        for num in nums:
            index = index ^ num
        return index
        