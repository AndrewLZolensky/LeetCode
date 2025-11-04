class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in index:
                return [i, index[complement]]
            index[num] = i
        return [0,0]

        