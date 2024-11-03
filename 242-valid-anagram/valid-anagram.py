class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if (len(s) != len(t)):
            return False

        freq = {}
        n = len(s)
        for i in range(n):
            s_sym = s[i]
            t_sym = t[i]
            if s_sym in freq.keys():
                freq[s_sym] += 1
            else:
                freq[s_sym] = 1
            if t_sym in freq.keys():
                freq[t_sym] -= 1
            else:
                freq[t_sym] = -1
        for key in freq.keys():
            num = freq[key]
            if num != 0:
                return False
        return True
        