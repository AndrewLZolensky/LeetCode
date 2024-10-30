class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        p = k % n
        rotated = [0] * n
        rotated[:p] = nums[(n-p):]
        rotated[p:] = nums[:(n-p)]
        for i in range(n):
            nums[i] = rotated[i]
