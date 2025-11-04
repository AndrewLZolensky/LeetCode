class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        lp = [1]
        for i in range(len(nums) - 1):
            next_val = lp[-1] * nums[i]
            lp.append(next_val)
        rp = [1]
        for i in range(1, len(nums)):
            next_val = rp[-1] * nums[-i]
            rp.append(next_val)
        rp.reverse()
        res = []
        for i in range(len(lp)):
            res.append(lp[i] * rp[i])
        return res

        