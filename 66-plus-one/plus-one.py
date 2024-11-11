class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        for i in range(1, len(digits) + 1):
            raw = digits[-i] + carry
            if raw >= 10:
                digits[-i] = raw % 10
                carry = 1
            else:
                digits[-i] = raw
                carry = 0
        if carry == 1:
            digits.insert(0, 1)
        
        return digits