class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        before_zero = list()
        for i in range(m):
            for j in range(n):
                if(matrix[i][j] == 0):
                    before_zero.append([i,j])
        for i in range(m):
            for j in range(n):
                if(matrix[i][j] == 0 and [i,j] in before_zero):
                    row= i
                    column =j
                    print(row,column)
                    for k in range(m):
                        for l in range(n):
                            if(k == row or l == column):
                                matrix[k][l] = 0
        print(matrix)
        