class Solution {
    public int removeDuplicates(int[] nums) {
        int bottom = 0;
        int prev = -(nums[0] + 1);
        for (int top = 0; top < nums.length; top++) {
            if (nums[top] != prev) {
                nums[bottom] = nums[top];
                bottom++;
            }
            prev = nums[top];
        }
        return bottom;
    }
}