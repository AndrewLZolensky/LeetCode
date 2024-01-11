class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_ix = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_ix:
                return [num_ix[complement], i]
            else:
                num_ix[num] = i
        return []