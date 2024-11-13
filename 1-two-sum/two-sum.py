class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        complements = {}
        for i in range(len(nums)):
            if nums[i] in complements.keys():
                return complements[nums[i]], i
            complements[target - nums[i]] = i