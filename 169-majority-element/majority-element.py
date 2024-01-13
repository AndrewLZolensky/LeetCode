class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        std = sorted(nums)
        maxrun = 0
        currun = 0
        maxel = 0
        prevel = std[0]
        for n in std:
            if n == prevel:
                currun += 1
            else:
                if (currun > maxrun):
                    maxrun = currun
                    maxel = prevel
                currun = 1
            prevel = n
        if (currun > maxrun):
            maxel = prevel
        return maxel
        