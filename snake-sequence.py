'''
Objective: Given two dimensional matrix, write an algorithm to find out the snake sequence which has the maximum length.
There could be many snake sequence in the matrix, you need to return the one with the maximum length.
Travel is allowed only in two directions, either go right OR go down.

What is snake sequence: Snake sequence can be made if number in adjacent right cell or number in the adjacent
down cell is either +1 or -1 from the number in the current cell.
'''

from PrintMatrix import printMatrix

def snake_seq(matrix):


    m = len(matrix)
    n = len(matrix[0])

    matrix1 = [[0 for x in range(n)] for y in range(m)]

    matrix1[0][0] = 1
    for x in range(1,n):
        if abs(matrix[0][x]-matrix[0][x-1]) == 1:
            matrix1[0][x] = matrix1[0][x-1]+ 1
        else:
            matrix1[0][x] = 1

    for y in range(1,m):
        if abs(matrix[y][0]-matrix[y-1][0]) == 1:
            matrix1[y][0] = matrix1[y-1][0]+ 1
        else:
            matrix1[y][0] = 1

    for x in range(1,m):
        for y in range(1,n):
            up_score = 0
            if abs(matrix[x][y]-matrix[x-1][y]) == 1:
                up_score = matrix1[x-1][y] +1
            else:
                up_score = 1

            left_score = 0
            if abs(matrix[x][y]-matrix[x][y-1]) == 1:
                left_score = matrix1[x][y-1] +1
            else:
                left_score = 1

            matrix1[x][y] = max(up_score,left_score)

    printMatrix(matrix1)


mat1 = [[1,2,1,2],[7,7,2,5],[6,4,3,4],[1,2,2,5]]
printMatrix(mat1)
snake_seq(mat1)