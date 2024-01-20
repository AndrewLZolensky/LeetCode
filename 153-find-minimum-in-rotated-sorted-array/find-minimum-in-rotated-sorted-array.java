class Solution {
    public int findMin(int[] nums) {
        int s = 0;
        int e = nums.length - 1;
        while (s < e) {
            int m = (s + e) / 2;
            if (nums[m] < nums[e]) {
                e = m;
            } else {
                s = m + 1;
            }
        }
        return nums[s];
    }
}