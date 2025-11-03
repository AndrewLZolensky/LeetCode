class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        if n == 1:
            return True
        
        tortoise = n
        hare = n

        while hare != 1:
            tortoise = self.sumSqDigits(tortoise)
            hare = self.sumSqDigits(self.sumSqDigits(hare))
            if tortoise == hare and hare != 1:
                return False
        return True
    
    def sumSqDigits(self, n):
        # sum square of digits
        str_n = str(n)
        n_digits = len(str_n)
        total_sum = 0
        for i in range(n_digits):
            total_sum += int(str_n[i])**2
        return total_sum
