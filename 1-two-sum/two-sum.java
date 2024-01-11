class Solution {
    public int[] twoSum(int[] nums, int target) {
        int n = nums.length;
        int complement;
        Map<Integer, Integer> numIx = new HashMap<>();

        for (int i=0; i < n; i++) {
            complement = target - nums[i];
            if (numIx.containsKey(complement)) {
                return new int[]{numIx.get(complement), i};
            } else {
                numIx.put(nums[i], i);
            }
        }

        return new int[]{};
    }
}