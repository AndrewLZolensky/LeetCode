int removeElement(int* nums, int numsSize, int val) {
    int s = 0;
    int e = numsSize;
    while (s < e) {
        if (nums[s] == val) {
            nums[s] = nums[e-1];
            e--;
        } else {
            s++;
        }
    }
    return s;
}