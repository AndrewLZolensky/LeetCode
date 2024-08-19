class Solution {
    public int minSteps(int n) {
        int curr = n;
        int steps = 0;
        for (int factor = 2; factor <= n; factor++) {

            // if i is a prime factor of curr
            while (curr % factor == 0) {

                // divide curr by prime factor
                curr  = curr / factor;

                // then add prime factor for copy + paste i-1 times
                steps += factor;
            }

            if (curr == 1) {
                break;
            }
        }

        return steps;
    }
}