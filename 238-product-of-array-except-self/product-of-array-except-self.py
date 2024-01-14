class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a1 = [1]
        a2 = [1]
        n = len(nums)
        for i in range(0, n-1):
            a1.append(a1[i]*nums[i])
            a2.append(a2[i]*nums[-(i+1)])
        answer = []
        for i in range(0, n):
            answer.append(a1[i]*a2[-(i+1)])

        
        return answer
        