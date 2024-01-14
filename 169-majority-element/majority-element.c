int majorityElement(int* nums, int numsSize) {
    int cand = 0;
    int count = 0;
    for (int i = 0; i < numsSize; i++) {
        cand = (count == 0) ? nums[i] : cand;
        count = (nums[i] == cand) ? count + 1 : count - 1;
    }
    return cand;
}