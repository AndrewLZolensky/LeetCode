class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        if n == 0:
            return 0
        
        counter = 0
        rev = 0
        while n > 0:
            mod = n % 2
            rev |= mod
            n //= 2

            counter += 1
            if counter < 32:
                rev <<= 1

        while counter < 31:
            rev <<= 1
            counter += 1
        return int(rev)
