class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        left = 0
        right = 0
        high = 0

        while right < len(prices):
            buy = prices[left]
            sell = prices[right]
            profit = sell - buy
            if sell < buy:
                left = right
            elif profit > high:
                high = profit
            right += 1
        
        return high
