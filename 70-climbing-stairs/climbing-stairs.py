class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        arr = [0] * n
        arr[:2] = [1, 2]
        for i in range(2, n):
            arr[i] = arr[i-1] + arr[i-2]
        return arr[n-1]
        