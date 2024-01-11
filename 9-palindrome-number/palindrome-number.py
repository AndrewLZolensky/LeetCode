class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        string_num = str(x)
        rev_string = string_num[::-1]
        if (string_num == rev_string):
            return True
        return False
        