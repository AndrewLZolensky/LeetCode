class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ns = len(s)
        nt = len(t)
        if ns != nt:
            return False
        seen = {}
        for i in range(ns):
            if s[i] in seen.keys():
                symbol = seen[s[i]]
                if t[i] != symbol:
                    return False
            else:
                if t[i] in seen.values():
                    return False
                seen[s[i]] = t[i]
        return True