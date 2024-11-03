class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0: # change for $0 is 0 coins
            return 0
        if len(coins) == 0: # no coins means no change
            return -1
        if amount < 0: # change for -$x cannot be made (-1)
            return -1
        mincoin = min(coins)
        if amount < mincoin: # change for amt < smallest coin cannot be made (-1)
            return -1

        amounts = [0] * (amount + 1) # init amounts = [0, -1, ..., 1, 0, ..., 0]
        for i in range(1, mincoin):
            amounts[i] = -1
        for i in range(mincoin, amount + 1):
            candidates = []
            for coin in coins:
                if coin <= i:
                    cand = amounts[i - coin]
                    if cand != -1:
                        candidates.append(cand + 1)
            if len(candidates) == 0:
                amounts[i] = -1
            else:
                amounts[i] = min(candidates)
        
        return amounts[amount]
