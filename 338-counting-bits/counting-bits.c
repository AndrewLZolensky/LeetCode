int numOnes(uint32_t n) {
    int n_steps = 8 * sizeof(uint32_t);
    int num_ones = 0;
    for (int i = 0; i < n_steps; i++) {
        if (n & 0x01) {
            num_ones++;
        }
        n >>= 1;
    }
    return num_ones;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* countBits(int n, int* returnSize) {
    *returnSize = n + 1;
    int* ans = malloc((n + 1) * sizeof(int));
    for (int i = 0; i <= n; i++) {
        ans[i] = numOnes((uint32_t) i);
    }
    return ans;
}