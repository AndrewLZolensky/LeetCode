class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        # s[i] = smallest needed to make amount i
        # s[i] = min({i - s[i-amt] for amt in coins}) + 1
        amounts = [0]
        for i in range(1, amount + 1):
            valid_coins = [c for c in coins if c <= i]
            candidates = [amounts[i - c] + 1 for c in valid_coins if amounts[i - c] >= 0]
            if len(candidates) == 0:
                amounts.append(-1)
            else:
                amounts.append(min(candidates))
        return amounts[amount]
        