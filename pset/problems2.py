'''
Write a function transpose() that accepts a 2D integer array matrix and returns the transpose of matrix. The transpose of a
 matrix is the matrix flipped over its main diagonal, swapping the rows and columns.
'''
'''
precond:
    -can it be 0x0
    -can it be a square
    -is space complexity an issue
'''
def solve(matrix=None):
    n = len(matrix)
    m = len(matrix[0])

    aux = [[0]*n for _ in range(m)]
    #Append the rows to aux matrix

    for i in range(len(matrix)): 
        for j in range(len(matrix[0])):
            aux[j][i] = matrix[i][j]
    print(aux)
    return aux

solve(matrix = [
    [1, 2, 3],
    [4, 5, 6]
])


