class Solution {
    public int climbStairs(int n) {
        // observe: we can reach stair n in "two" wayss
        // one: go to stair n-1 then take a step
        // two: go to stair n-2 then take a two-step
        // thus, ways(n) = ways(n-1) + ways(n-2)
        int[] ways = new int[n];


        // tabulate
        for (int i = 0; i < n; i++) {

            // base case 1: 1 stair -> 1 way
            if (i == 0) {
                ways[i] = 1;
            // base case 2: 2 stairs -> 2 ways
            } else if (i == 1) {
                ways[i] = 2;
            // otherwise fibonacci
            } else {
                ways[i] = ways[i-1] + ways[i-2];
            }

        }

        return ways[n-1];
    }
}