class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = set()
        col = set()
        n = len(matrix)         # num of rows
        m = len(matrix[0])      # num of cols

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:       # any row with 0 add col and row
                    row.add(i)
                    col.add(j)
        
        for i in range(n):
            for j in range(m):
                if i in row or j in col:            # row col with 0, put 0
                    matrix[i][j] = 0