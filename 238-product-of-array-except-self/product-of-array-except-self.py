class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a1 = [1]
        a2 = [1]
        for i in range(0, len(nums)-1):
            a1.append(a1[i]*nums[i])
            a2.append(1)
        for i in range(1, len(nums)):
            a2[-(i+1)] = a2[-i]*nums[-i]
        answer = []
        for i in range(0, len(nums)):
            answer.append(a1[i]*a2[i])

        
        return answer
        