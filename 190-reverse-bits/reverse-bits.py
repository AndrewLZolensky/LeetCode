class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        rev = 0
        for i in range(32):
            rev |= (n & 1)
            if i < 31:
                rev <<= 1
                n >>= 1
        return rev

