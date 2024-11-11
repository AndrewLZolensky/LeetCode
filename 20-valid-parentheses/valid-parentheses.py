class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        closed_to_open = {')': '(', '}': '{', ']': '['} # store pairings
        openers = ['(', '{', '[']
        stack = []

        for c in s:
            if c in openers:
                stack.append(c)
            else:
                if not stack or stack.pop() != closed_to_open[c]:
                    return False

        return len(stack) == 0
