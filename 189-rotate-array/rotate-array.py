class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        rotated = [0] * n
        for i in range(n):
            index = int((i + k) % n)
            rotated[index] = nums[i]
        for i in range(n):
            nums[i] = rotated[i]
        