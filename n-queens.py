from copy import copy, deepcopy

matrix_orig = [[0 for x in range(8)] for y in range(8)]
total_sols = 0
def nqueens(matrix, n, idx=0):
    global total_sols
    if idx >= n:
        print matrix
        total_sols += 1
        return
    #nw_matrix = [row[:] for row in matrix]

    #nw_matrix = deepcopy(matrix)
    for i in range(n):
        nw_matrix = deepcopy(matrix)
        if ispossible(nw_matrix,i,idx):
            nw_matrix[i][idx] = 1
            nqueens(nw_matrix,n,idx+1)


def ispossible(matrix,i,idx):
    #check ith row until idx column
    for x in range(idx):
        if matrix[i][x] == 1:
            return False

    #check idx column until ith row
    for y in range(i):
        if matrix[y][idx] == 1:
            return False

    row = i-1
    col = idx-1
    # check upward diagonal
    while row >= 0 and col >=0:
        if matrix[row][col] == 1:
            return False
        row -= 1
        col -= 1

    row = i+1
    col = idx-1
    #check downward diagonal
    while row <= len(matrix)-1 and col >= 0:
        if matrix[row][col] == 1:
            return False
        row += 1
        col -= 1

    return True


nqueens(matrix_orig,8)
print "total sols found: ", total_sols

def test_copy(matrix,idx):
    if idx >= 8:
        return

    nw_matrix = deepcopy(matrix)
    test_copy(nw_matrix,idx+1)
    nw_matrix[0][idx] = 1
    print nw_matrix

#test_copy(matrix_orig,0)





