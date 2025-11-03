class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_hyp = 0
        hyp = ""
        for i in range(len(s)):

            # add next char to hypothesis
            next_char = s[i]
            hyp += next_char

            # trace back through hypothesis and terminate at first dup occurrence
            for j in range(2, len(hyp) + 1):
              if hyp[-j] == next_char:
                hyp = hyp[-j + 1:]
                break
            
            # check if hyp longer than max
            if len(hyp) >= max_hyp:
              max_hyp = len(hyp)

            
        
        return max_hyp
        