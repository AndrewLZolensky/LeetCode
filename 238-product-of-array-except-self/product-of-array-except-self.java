class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] answer = new int[n];
        answer[0] = 1;

        int leftmul = 1;
        for (int i = 0; i < n - 1; i++) {
            leftmul *= nums[i];
            answer[i+1] = leftmul;
        }
        int rightmul = 1;
        for (int i = n - 1; i > 0 ; i--) {
            rightmul *= nums[i];
            answer[i-1] *= rightmul;
        }

        return answer;
    }
}