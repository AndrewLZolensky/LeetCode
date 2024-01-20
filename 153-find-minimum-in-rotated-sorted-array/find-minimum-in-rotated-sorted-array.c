int findMin(int* nums, int numsSize) {
    int* start = nums;
    int* end = nums + (numsSize - 1);
    while (start < end) {
        int* middle = start + (end - start) / 2;
        if (*middle < *end) {
            end = middle;
        } else {
            start = middle + 1;
        }
    }
    return *start;
}