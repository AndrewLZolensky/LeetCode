class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        p = k % n
        nums[:p], nums[p:] = nums[(n-p):], nums[:(n-p)]
