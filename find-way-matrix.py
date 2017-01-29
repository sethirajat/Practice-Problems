'''
in a grid, the numbers represent sea levels. You can move in all 4 directions if the maximum difference between the two levels is 1
you have to find out if the path exists between 2 levels.
'''
import time

def get_neighbours(matrix,start):
    current = matrix[start[0]][start[1]]
    row = start[0]
    col = start[1]
    neighbours = []
    #left
    if col -1 >= 0 and abs(matrix[row][col-1]-current) <= 1:
        neibh = (row,col-1)
        neighbours.append(neibh)
    #up
    if row -1 >= 0 and abs(matrix[row-1][col]- current) <= 1:
        neibh = (row-1,col)
        neighbours.append(neibh)

    #right
    if col+1 < len(matrix[0]) and abs(matrix[row][col+1] - current) <= 1:
        neibh = (row , col+1)
        neighbours.append(neibh)

    #down
    if row+1 < len(matrix) and abs(matrix[row+1][col] - current) <= 1:
        neibh = (row +1 , col)
        neighbours.append(neibh)

    return neighbours


def find_way(matrix, start, stop):
    visited = set()

    queue = []

    queue.append(start)
    while len(queue) > 0:
        elem = queue.pop(0)
        #print "element is : ", elem
        if elem == stop:
            return True

        if elem in visited:
            continue
        visited.add(elem)
        for element in get_neighbours(matrix, elem):
            if element not in visited:
                queue.append(element)

    return False

def find_way_rec(matrix,start,stop,visited = None):
    if visited is None:
        visited = set()

    #print "start is: ", start
    if start == stop:
        return True
    if start in visited:
        return False
    visited.add(start)
    row = start[0]
    col = start[1]
    current = matrix[row][col]

    #right
    if col+1 < len(matrix[0]) and abs(current - matrix[row][col+1]) <= 1:
        new = (row,col+1)
        if find_way_rec(matrix,new,stop,visited):
            return True

    #down
    if row+1 < len(matrix) and abs(current-matrix[row+1][col]) <= 1:
        new = (row+1,col)
        if find_way_rec(matrix,new,stop,visited):
            return True

    #up
    if row-1 >= 0 and abs(current-matrix[row-1][col]) <= 1:
        new = (row-1,col)
        if find_way_rec(matrix,new,stop,visited):
            return True

    #left
    if col-1 >= 0 and abs(current - matrix[row][col-1]) <= 1:
        new = (row,col-1)
        if find_way_rec(matrix,new,stop,visited):
            return True

    return False



#arr = [[1,2,3,4],[6,1,7,8], [9,0,5,8],[2,2,1,2]]
arr = [[1,2,3,4,-4],[0,3,4,5,-8],[9,5,7,6,-12],[13,6,8,9,-16],[17,7,9,10,11]]
start_time = time.time()
for x in range(100):
    find_way(arr, (0, 0), (4, 4))
    '''
    if find_way(arr, (0, 0), (4, 4)):
        print "way found"
    else:
        print "way not found"
    '''
print("normal one took %s second" % (time.time() - start_time))

start_time = time.time()
for x in range(100):
    find_way_rec(arr, (0, 0), (4, 4))
    '''
    if find_way_rec(arr, (0, 0), (4, 4)):
        print "recur way found"
    else:
        print "recur way not found"
    '''
print("rec one took %s second" % (time.time() - start_time))