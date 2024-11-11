class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry = 0
        a_len = len(a)
        b_len = len(b)
        max_len = max(a_len, b_len)
        total = ""
        for i in range(1, max_len + 1):
            a_el = int(a[-i]) if i <= a_len else 0
            b_el = int(b[-i]) if i <= b_len else 0
            bitsum = carry + a_el + b_el
            if bitsum == 0:
                total += "0"
                carry = 0
            elif bitsum == 1:
                total += "1"
                carry = 0
            elif bitsum == 2:
                total += "0"
                carry = 1
            else:
                total += "1"
                carry = 1
        if carry == 1:
            total += "1"
        
        return total[::-1]