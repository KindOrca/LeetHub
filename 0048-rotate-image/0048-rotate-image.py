class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        L = len(matrix)
        for i in range(L//2):
            for j in range(L//2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[L-1-j][i]
                matrix[L-1-j][i] = matrix[L-1-i][L-1-j]
                matrix[L-1-i][L-1-j] = matrix[j][L-1-i]
                matrix[j][L-1-i] = temp
        if L % 2 != 0:
            for i in range(L//2):
                temp = matrix[L//2][i]
                matrix[L//2][i] = matrix[L-1-i][L//2]
                matrix[L-1-i][L//2] = matrix[L//2][L-1-i]
                matrix[L//2][L-1-i] = matrix[i][L//2]
                matrix[i][L//2] = temp