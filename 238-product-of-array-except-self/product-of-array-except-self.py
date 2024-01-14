class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        answer = [1] * n

        leftmul = 1
        for i in range(n-1):
            leftmul *= nums[i]
            answer[i+1] *= leftmul
        
        rightmul = 1
        for i in range(1, n):
            rightmul *= nums[-i]
            answer[-(i+1)] *= rightmul

        return answer
        