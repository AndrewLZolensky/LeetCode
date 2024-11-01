class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        return self.gen(n, 0)

    def gen(self, k, add):
        if (k == 1):
            return [[1 + add]]
        
        if (k == 2):
            return [[1 + add,2 + add],[4 + add,3 + add]]

        mat = [[0] * k for i in range(k)]
        for i in range(k-1):
            mat[0][i] = i + 1 + add
            mat[i][k - 1] = k + i + add
            mat[k - 1][k - 1 - i] = 2 * k - 1 + i + add
            mat[k - 1 - i][0] = 3 * k - 2 + i + add
            
        middle = self.gen(k-2, mat[1][0])
        for i in range(1, k-1):
            mat[i][1:k-1] = middle[i-1]
        return mat
