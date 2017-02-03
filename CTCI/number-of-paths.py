'''
Q-8.2
Imagine a robot sitting on the upper left hand corner of an NxN grid. The robot can only move in two directions: right and down. How many possible paths are there for the robot?
FOLLOW UP
Imagine certain squares are "off limits", such that the robot can not step on them. Design an algorithm to get all possible paths for the robot.
'''
total_count = 0
def find_number_of_paths(matrix,row,col,size):
    global total_count
    if row == size-1 and col == size-1:
        total_count += 1
        return

    if row >= size or col >= size:
        return

    #move right
    if col+1 < size:
        find_number_of_paths(matrix,row,col+1,size)

    #move down
    if row+1 < size:
        find_number_of_paths(matrix, row + 1, col, size)



arr = [[1,2,3,4,-4],[0,3,4,5,-8],[9,5,7,6,-12],[13,6,8,9,-16],[17,7,9,10,11]]
find_number_of_paths(arr,0,0,5)
print "total paths  for 5X5 matrix are: ", total_count



