class Solution {
    public int coinChange(int[] coins, int amount) {
        // initialize array = infty of size 0:amount
        // array[0] = 0
        // for amt in 1:amount
        // array[amt] = min{coinChange(amt-coin) + 1 | coin in coins, amt-coin >= 0, coinChange(amt-coin) != infty}
        int[] array = new int[amount + 1];
        for (int i = 0; i <= amount; i++) {
            array[i] = amount + 1;
        }
        array[0] = 0;
        for (int i = 1; i <= amount; i++) {
            for (int coin : coins) {
                if ((i - coin >= 0) && (array[i-coin] != amount + 1)) {
                    if (array[i-coin] + 1 < array[i]) {
                        array[i] = array[i-coin] + 1;
                    }
                }
            }
        }

        int res = array[amount];
        if (res == amount + 1) {
            return -1;
        }

        return res;
    }
}