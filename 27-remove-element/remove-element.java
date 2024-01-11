class Solution {
    public int removeElement(int[] nums, int val) {
        int le = nums.length;
        int k = nums.length;
        int ix = 0;
        while (ix < le) {
            if (nums[ix] != val) {
                ix++;
            } else {
                k--;
                nums[ix] = nums[le - 1];
                le--;
            }
        }

        return k;
    }
}