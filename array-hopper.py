'''
program to find the minimum hps from one end of an array to another. ) means you cannot go to that index
'''
import sys
min_count = sys.maxint
def min_hops(arr, i, cur_count, curr_path = []):
    global min_count
    if i >= len(arr)- 1:
        if min_count > cur_count:
            min_count = cur_count
            print "current path: ", curr_path
        return

    if arr[i] == 0:
        return
    curr_path.append(arr[i])
    for x in range(1, arr[i]+1):
        min_hops(arr,i+x,cur_count+1,curr_path[:])


def min_hops_dp(arr):
    n = len(arr)
    jumps = []

    jumps.append(0)

    for x in range(1, n):
        min_hop = sys.maxint
        for y in range(x):
            if arr[y] + y >= x:
                if jumps[y] < min_hop:
                    min_hop = jumps[y] +1
            jumps.append(min_hop)

    return jumps[-1]

def min_hops_nw(arr):
    hops = 0
    curr = 0
    while curr < len(arr)-1:
        maxhop = 0
        maxelem = 0
        for x in range(1,arr[curr]+1):
            if x >= len(arr)-1:
                return hops+1
            if arr[curr+x] == 0:
                continue
            currhop = curr + x + arr[curr+x]
            if currhop > maxhop:
                maxhop = currhop
                maxelem = x
        curr += maxelem
        hops += 1
        if maxhop >= len(arr)-1:
            return hops+1

    return hops



#arr = [4,2,1,5,0,3,1,1,1,2,1]
arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
arr1 = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
min_hops(arr,0,0)
print "min hops found from rec call are: ", min_count
print "min call from dp is: ", min_hops_dp(arr)
print "min call from new is: ", min_hops_nw(arr)





