class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split(" ")
        symbols = list(pattern)
        if (len(words) != len(symbols)):
            return False
        bindings = {}
        for i in range(len(words)):
            symbol = symbols[i]
            if (symbol in bindings.keys()):
                exp_val = bindings[symbol]
                if (words[i] != exp_val):
                    return False
            else:
                if (words[i] in bindings.values()):
                    return False # if find new symbol aassoc to old word
                bindings[symbol] = words[i]
        return True        