class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        modded = " ".join(s.split())
        return len(modded.split(" ")[-1])
        