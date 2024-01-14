class Solution {
    public int removeDuplicates(int[] nums) {
        int bottom = 1;
        for (int top = 1; top < nums.length; top++) {
            if (nums[top] != nums[top-1]) {
                nums[bottom] = nums[top];
                bottom++;
            }
        }
        return bottom;
    }
}