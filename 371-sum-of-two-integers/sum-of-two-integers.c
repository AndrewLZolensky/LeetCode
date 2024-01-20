int getSum(int a, int b) {

    // get the number of bits in an unsigned int
    int n_steps = 8 * sizeof(unsigned int);
    unsigned int ua = (unsigned int) a;
    unsigned int ub = (unsigned int) b;
    unsigned int sum_bit = 0;
    unsigned int carry_bit = 0;
    unsigned int result = 0;

    for (int i = 0; i < n_steps; i++) {
        unsigned int mua = ua & 0x01;
        unsigned int mub = ub & 0x01;
        sum_bit = (mua ^ mub) ^ carry_bit;
        carry_bit = (mua & mub) | (mua & carry_bit) | (mub & carry_bit);
        result |= (sum_bit << i);
        ua >>= 1;
        ub >>= 1;
    }

    signed int result_signed = (signed int) result;
    return result_signed;
}