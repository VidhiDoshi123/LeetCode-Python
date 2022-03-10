class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
       
        m = len(matrix)
        n = len(matrix[0]) 
        for i in range(m):
            for j in range(i+1,n):
                matrix[i][j] , matrix[j][i] = matrix[j][i], matrix[i][j]
        print("hello")
        print(matrix)
        for i in range(m):
            row = matrix[i]
            start = 0
            end = len(row) -1
            while(start < end):
                row[start], row[end] = row[end] ,row[start]
                start = start + 1
                end = end -1
        print(matrix)
        
        