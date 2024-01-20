class Solution {
    public int findMin(int[] nums) {
        int start = 0;
        int end = nums.length - 1;
        while (start < end) {
            int middle = (start + end) / 2;
            if (nums[middle] < nums[end]) {
                end = middle;
            } else {
                start = middle + 1;
            }
        }
        return nums[start];
    }
}