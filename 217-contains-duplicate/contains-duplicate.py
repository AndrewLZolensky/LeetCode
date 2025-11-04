class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        index = {}
        for num in nums:
            if num in index:
                return True
            index[num] = None
        return False
        