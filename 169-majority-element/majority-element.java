class Solution {
    public int majorityElement(int[] nums) {
        int count = 0;
        int cand = 0;
        for (int i = 0; i < nums.length; i++) {
            cand = (count == 0) ? nums[i] : cand;
            count = (nums[i] == cand) ? count + 1 : count - 1;
        }
        return cand;
    }
}