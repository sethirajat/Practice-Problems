board = [0]*30
min_throws = 100
#add ladders
board[4] = 7
board[2] = 21
board[10] = 25
board[19] = 28
board[26] = 0
board[20] = 9
board[16] = 4
board[18] = 7

def find_min_throws(board,throw=0, idx =0):
    if idx >= len(board)-1:
        return
    if board[idx] != 0 and board[idx] < idx:
        find_min_throws(board,throw,board[idx])
        return

    global min_throws
    if idx + 6 >= len(board)-1:
        new_throw = throw + 1
        if new_throw < min_throws:
            min_throws = new_throw
        return

    for i in range(1,7):
        if board[idx+i] > idx+i:
            find_min_throws(board,throw+1,board[idx+i])

    while i > 0:
        if board[idx+i] == 0 or board[idx+i] > idx+i:
            if board[idx+i] > idx+i:
                break
            else:
                find_min_throws(board,throw+1,idx+i)
                break
        i -= 1


find_min_throws(board)
print "min throws are: ", min_throws

for i in range(1,7):
    print i

print "now is: ", i

