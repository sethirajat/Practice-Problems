def printMatrix(matrix):
    Y = len(matrix)
    print "=== Start of Matrix==="
    for row in matrix:
        for val in row:
            print '{:{}}'.format(val, Y),
        print

    print "=== End of Matrix==="