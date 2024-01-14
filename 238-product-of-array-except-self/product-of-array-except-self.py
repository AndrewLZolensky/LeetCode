class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = [1]
        a2 = [1]
        n = len(nums)
        for i in range(0, n-1):
            answer.append(answer[i]*nums[i])
            a2.append(a2[i]*nums[-(i+1)])
        for i in range(0, n):
            answer[i] = answer[i]*a2[-(i+1)]

        return answer
        