class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        rev = 0
        for _ in range(32):
            rev <<= 1
            rev |= (n & 1)
            n >>= 1
        return rev

