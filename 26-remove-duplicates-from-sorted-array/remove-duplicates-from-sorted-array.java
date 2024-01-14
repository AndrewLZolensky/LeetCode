class Solution {
    public int removeDuplicates(int[] nums) {
        int top = 0;
        int bottom = 0;
        int prev = -(nums[0] + 1);
        while (top < nums.length) {
            if (nums[top] != prev) {
                nums[bottom] = nums[top];
                bottom++;
            }
            prev = nums[top];
            top++;
        }
        return bottom;
    }
}