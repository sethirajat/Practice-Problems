'''
Progarm to implement binary search
'''

def bin_search_iterative(Arr,num):

    left = 0
    right = len(Arr)-1

    while left <= right:
        mid = int((left+right)/2)
        if Arr[mid] == num:
            return mid
        if Arr[mid] < num:
            left = mid+1
        else:
            right = mid-1

    return -1

arr = [4,6,8,10,15,20,40,100,1000,1020,1021]

ret = bin_search_iterative(arr,40)
print "40 is found at pos: ", ret

tofind = int(raw_input("enter number to find\n"))
ret1 = bin_search_iterative(arr,tofind)
if ret1 != -1:
    print tofind, " is found at pos: ", ret1
else:
    print tofind, " was not found"

