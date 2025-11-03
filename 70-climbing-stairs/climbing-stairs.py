class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return 1
        nums = [1, 1]
        for i in range(n - 1):
            nums.append(nums[-1] + nums[-2])
        return nums[-1]
        