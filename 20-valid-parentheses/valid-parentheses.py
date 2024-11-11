class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if len(s) == 0: # empty is valid
            return True
        
        closed_to_open = {')': '(', '}': '{', ']': '['} # store pairings
        stack = []
        for c in s:
            if len(stack) > 0: # catch case with no open bracket
                last = stack[-1]
            else:
                last = None
            if c in closed_to_open.keys(): # if closed
                if last == closed_to_open[c]: # if match last parentheses, pop
                    stack.pop()
                else:
                    return False # if the current parentheses is closed but not correct, return False
            # if the current parentheses is open, add it
            else:
                stack.append(c)
        
        if len(stack) > 0:
            return False
        return True
