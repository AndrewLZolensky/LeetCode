class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxp = 0
        running = 0
        for i in range(len(prices) - 1):
            gain = prices[i+1] - prices[i]
            # if we lose money this day, update max
            if gain < 0:
                if running > maxp:
                    maxp = running
            running += gain
            if running < 0:
                running = 0
        # check last pair
        if running > maxp:
            maxp = running
        return maxp