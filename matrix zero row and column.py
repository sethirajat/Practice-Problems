'''
Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column is set to 0.
'''

from PrintMatrix import printMatrix

def make_zero(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    zero_rows = [False]*rows
    zero_cols = [False]*cols

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                zero_rows[i] = True
                zero_cols[j] = True

    for i in range(rows):
        for j in range(cols):
            if zero_rows[i] or zero_cols[j]:
                matrix[i][j] = 0


mat1 = [[1,2,3,4,-4],[5,6,7,8,-8],[9,10,11,12,-12],[13,14,15,16,-16],[17,18,19,20,0]]

print "before making zeroes"
printMatrix(mat1)
make_zero(mat1)
print "after making zeroes"
printMatrix(mat1)




