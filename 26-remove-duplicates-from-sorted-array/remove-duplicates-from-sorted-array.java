class Solution {
    public int removeDuplicates(int[] nums) {
        int j = 1;
        int l = nums.length;
        System.gc();
        for (int i = 1; i < l; i++) {
            if (nums[i] != nums[i-1]) {
                nums[j] = nums[i];
                j++;
            }
        }
        return j;
    }
}