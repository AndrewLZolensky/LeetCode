class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        contrast = {
            '(':')',
            '[':']',
            '{':'}'
        }

        opener = ['(','[','{']

        stack = []


        for item in s:
            if item in contrast:
                stack.append(item)
            else:
                if not stack or contrast[stack.pop()] != item:
                    return False
            

        return len(stack) == 0
