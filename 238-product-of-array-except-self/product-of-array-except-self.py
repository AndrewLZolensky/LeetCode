class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        lp = [1]
        rp = [1]
        for i in range(len(nums) - 1):
            next_lval = lp[-1] * nums[i]
            next_rval = rp[-1] * nums[-i - 1]
            lp.append(next_lval)
            rp.append(next_rval)
        rp.reverse()
        res = []
        for i in range(len(lp)):
            res.append(lp[i] * rp[i])
        return res

        