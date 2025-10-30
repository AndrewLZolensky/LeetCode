class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        # init triangle
        triangle = []

        # add each row
        for i in range(numRows):

            # handle special cases
            if i == 0:
                triangle.append([1])
                continue
            if i == 1:
                triangle.append([1,1])
                continue

            # compute new row
            new_row = [1]

            # compute each component as sum of components above it
            previous_row = triangle[i-1]
            for j in range(len(previous_row) - 1):
                new_row.append(previous_row[j] + previous_row[j + 1])
            new_row.append(1)

            # append new row
            triangle.append(new_row)
        
        return triangle
        