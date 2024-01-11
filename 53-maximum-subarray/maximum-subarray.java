class Solution {
    public int maxSubArray(int[] nums) {
        // kadane algorithm
        int max = nums[0];
        int curr = 0;
        
        for (int num : nums) {
            curr = curr > 0 ? curr + num : num;
            max = curr > max ? curr : max;
        }

        return max;
    }
}