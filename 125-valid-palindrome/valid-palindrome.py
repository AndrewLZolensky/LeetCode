class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        s = "".join([c for c in s if c.isalnum()])
        n = len(s)

        if n == 0 or n == 1:
            return True
        
        stack = []
        i1 = 0
        i2 = 0
        while i2 < n - 1:
            stack.append(s[i1])
            i1 += 1
            i2 += 2
        
        if i2 == n - 1:
            i1 += 1
        
        while i1 < n:
            if s[i1] != stack.pop():
                return False
            i1 += 1
        
        return True
        