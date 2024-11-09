class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = 0
        while n > 1:
            num += n % 2
            n /= 2
        num += 1
        return num
        