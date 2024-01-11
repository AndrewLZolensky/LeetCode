class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        values = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }

        n = len(s)
        count = 0
        last_value = 0

        for c in s:
            curr_value = values[c]
            count += curr_value
            if curr_value > last_value:
                count -= 2*last_value
            last_value = curr_value
        return count
