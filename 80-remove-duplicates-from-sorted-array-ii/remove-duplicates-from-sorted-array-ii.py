class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        write = 0
        read = 0
        prev1 = 0.5
        prev2 = 0.5
        while (read < len(nums)):
            if (nums[read] == prev2):
                pass
            else:
                nums[write] = nums[read]
                write += 1
            prev2 = prev1
            prev1 = nums[read]
            read += 1
        return write
        