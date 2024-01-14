class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxP = 0
        left = 0
        right = 1
        while right < len(prices):
            gain = prices[right] - prices[left]
            if gain > 0:
                maxP = max(gain, maxP)
            else:
                left=right
            right += 1
        return maxP
