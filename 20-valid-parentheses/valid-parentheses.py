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
            if c in closed_to_open.values():
                stack.append(c)
            else:
                if not stack or stack[-1] != closed_to_open[c]:
                    return False
                stack.pop()

        return len(stack) == 0
