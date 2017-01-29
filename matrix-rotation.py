'''
Program to rotate a matrix
'''


def printMatrix(matrix):
    Y = len(matrix)
    print "=== Start of Matrix==="
    for row in matrix:
        for val in row:
            print '{:{}}'.format(val, Y),
        print

    print "=== End of Matrix==="


def rotate_matrix_in_place(matrix):

    #let the matrix be nXn
    if len(matrix) < 2:
        return
    n = len(matrix[0])
    if n < 2:
        return

    layers = int(n/2)
    for i in range(layers):
        start = i
        end = n-start-1

        for j in range(start,end):
            top = matrix[start][j]

            #left to top
            #left = matrix[end-j][start]
            left = matrix[end - j + start][start]
            matrix[start][j] = left

            #bottom to left
            #bottom = matrix[end][end-j]
            bottom = matrix[end][end - j + start]
            matrix[end - j + start][start] = bottom

            #right to bottom
            right = matrix[j][end]
            matrix[end][end - j + start] = right

            #top to right
            matrix[j][end] = top
            #print the matrix at this stage
            #printMatrix(matrix)

def transpose_matrix(matrix):
    n = len(matrix)
    end = int(n/2)
    for i in range(n):
        for j in range(i,n):
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

def rotate_using_transpose(matrix):
    transpose_matrix(matrix)
    start = 0
    end = len(matrix)-1

    while start < end:
        for j in range(len(matrix)):
            matrix[j][start],matrix[j][end] = matrix[j][end],matrix[j][start]
        start +=1
        end -=1


mat1 = [[1,2,3,4,-4],[5,6,7,8,-8],[9,10,11,12,-12],[13,14,15,16,-16],[17,18,19,20,-20]]
print "matrix before rotation and transpose:"
printMatrix(mat1)
print "matrix after transpose rotate: "
rotate_using_transpose(mat1)
printMatrix(mat1)
rotate_matrix_in_place(mat1)
print "matrix after rotation: "
printMatrix(mat1)