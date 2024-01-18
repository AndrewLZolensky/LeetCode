class Solution {
    public int maxProduct(int[] nums) {
        int maxprod = nums[0], minprod = nums[0], ans = nums[0];
        int maxtemp, mintemp;

        for (int i = 1; i < nums.length; i++) {
            int n = nums[i];
            maxtemp = maxprod*n;
            mintemp = minprod*n;
            maxprod = Math.max(maxtemp, Math.max(mintemp, n));
            minprod = Math.min(maxtemp, Math.min(mintemp, n));
            ans = Math.max(ans, maxprod);
        }

        return ans;
    }
}