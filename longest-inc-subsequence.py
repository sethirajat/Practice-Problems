'''
program to find longest increasing subsequence
'''


def LIS(arr,end):
    global maxims
    if len(arr) < 1:
        return 0
    if(maxims[end]) >0:
        return maxims[end]


    if end == 0:
        return 1
    maxim = 1
    for x in range(end):
        curr_lis = LIS(arr,x)
        if arr[x] < arr[end]:
           maxim = max(curr_lis+1,maxim)

    maxims[end] = maxim
    return maxim

def LIS_iterative(arr):
    if len(arr) < 1:
        return 0
    maximums = []
    maximums.append(1)
    for x in range(1,len(arr)):
        maxim = 1
        for y in range(x):
            if arr[y] < arr[x]:
                maxim = max(maximums[y]+1,maxim)
        maximums.append(maxim)

    return max(maximums)

ar = [8,1,4,22,9,-2,25]
maxims = [0] * len(ar)
LIS(ar,len(ar)-1)
print "LIS is: ", max(maxims)
print "LIS iter is: ", LIS_iterative(ar)