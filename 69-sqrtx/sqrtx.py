class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x
        
        low = 1
        high = x // 2
        while not (high < low):
            mid = (low + high)//2
            sq = mid * mid
            if sq == x:
                return mid
            if sq > x:
                high = mid - 1
            else:
                low = mid + 1
        return high