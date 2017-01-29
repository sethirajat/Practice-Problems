'''
Objective: Given two dimensional matrix, write an algorithm to count all possible paths from top left corner to bottom-right corner.
You are allowed to move only in two directions, move right OR move down.
There are few obstructions as well, means few cells are blocked and you cannot travel that cell.
Many times this problem is being referred as "Robot Travel Problem". Given a 2d matrix,
how many ways a robot can travel from top left corner to bottom right corner and there are few cells in which robot cannot travel.
'''

from PrintMatrix import printMatrix

def possible_paths(matrix):
    m = len(matrix)
    n = len(matrix[0])

    mat1 = [[0 for x in range(n)] for x in range(m)]
    if matrix[0][0] != -1:
        mat1[0][0] = 1
    for x in range(1,m):
        if matrix[x][0] != -1 and matrix[x-1][0] != -1:
            mat1[x][0] = 1

    for y in range(1,n):
        if matrix[0][y] != -1 and matrix[0][y-1] != -1:
            mat1[0][y] = 1

    for x in range(1,m):
        for y in range(1,n):
            if matrix[x][y] == -1:
                continue
            else:
                top_count = 0
                left_count = 0
                if matrix[x-1][y] != -1:
                    top_count = mat1[x-1][y]
                if matrix[x][y-1] != -1:
                    left_count = mat1[x][y-1]

                mat1[x][y] = top_count+left_count

    printMatrix(mat1)
    return mat1[m-1][n-1]


mat1 = [[1,1,1],[1,-1,1],[1,-1,1]]
printMatrix(mat1)
print "possible paths are: ", possible_paths(mat1)



