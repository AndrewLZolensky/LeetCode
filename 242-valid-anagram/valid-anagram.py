class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if (len(s) != len(t)):
            return False

        s_freq = {}
        t_freq = {}
        n = len(s)
        for i in range(n):
            s_sym = s[i]
            t_sym = t[i]
            if s_sym in s_freq.keys():
                s_freq[s_sym] += 1
            else:
                s_freq[s_sym] = 1
            if t_sym in t_freq.keys():
                t_freq[t_sym] += 1
            else:
                t_freq[t_sym] = 1
        for key in s_freq.keys():
            num = s_freq[key]
            if key not in t_freq.keys() or t_freq[key] != num:
                return False
        return True
        