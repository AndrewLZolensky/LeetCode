int hammingWeight(uint32_t n) {
    int num_bits = 8 * sizeof(uint32_t);
    int num_ones = 0;
    uint32_t cpy = n;
    for (int i = 0; i < num_bits; i++) {
        if (cpy & 0x01) {
            num_ones++;
        }
        cpy >>= 1;
    }
    return(num_ones);
}