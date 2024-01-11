int maxSubArray(int* nums, int numsSize) {
    int max = nums[0];
    int curr = 0;

    for (int i=0; i < numsSize; i++) {
        curr = curr >= 0 ? curr + *(nums+i) : *(nums+i);
        max = curr > max ? curr : max;
    }

    return max;
}