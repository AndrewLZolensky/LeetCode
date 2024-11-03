class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        m = n
        while (m > 1):
            if m % 2 != 0:
                return False
            m /= 2
        return True
        
        
        