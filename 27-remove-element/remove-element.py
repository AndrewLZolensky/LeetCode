class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        s = 0
        e = len(nums)
        while (s < e):
            if (nums[s] == val):
                nums[s] = nums[e-1]
                e -= 1
            else:
                s += 1
        return s