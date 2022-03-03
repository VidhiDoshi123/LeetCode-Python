class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        zero_row = list()
        zero_col = list()
        for i in range(m):
            for j in range(n):
                if(matrix[i][j]==0):
                    zero_row.append(i)
                    zero_col.append(j)
        for i in range(m):
            for j in range(n):
                if(i in zero_row or j in zero_col):
                    matrix[i][j] = 0
        
        