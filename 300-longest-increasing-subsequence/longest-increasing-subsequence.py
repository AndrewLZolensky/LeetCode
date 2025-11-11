class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # s[i] = length of longest subseq. ending in nums[i]
        # s[i] = min({s[i-j] + 1 | 1 <= j <= i, nums[i-j] < nums[i]})
        
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        
        s = [1]
        for i in range(1, len(nums)):
            curr = nums[i]
            cands = [s[i-j] for j in range(1,i+1) if nums[i-j] < curr]
            if len(cands) == 0:
                s.append(1)
            else:
                s.append(max(cands) + 1)
        return max(s)


        