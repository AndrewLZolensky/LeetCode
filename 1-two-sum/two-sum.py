class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        complements = {}
        for i, num in enumerate(nums):
            if num in complements:
                return complements[num], i
            complements[target - num] = i