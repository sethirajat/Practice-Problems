'''
Given an array A[] and a number x, check for pair in A[] with sum as x
'''

def find_sum_pair(A,x):
    if len(A) < 2:
        raise Exception( "can't find a pair")
    set1 = set()
    result = []
    for num in A:
        if x-num in set1:
            result.append([num,x-num])
        set1.add(num)
    return result


A = [1, 4, 45, 6, 10, -8]
n = 16

print find_sum_pair(A,n)

'''
Below code is from geeks for geeks, just for testing
'''

# Python program to find if there are two elements wtih given sum
CONST_MAX = 100000


# function to check for the given sum in the array
def printPairs(arr, arr_size, sum):
    # initialize hash map as 0
    binmap = [0] * CONST_MAX

    for i in range(0, arr_size):
        temp = sum - arr[i]
        if (temp >= 0 and binmap[temp] == 1):
            print "Pair with the given sum is", arr[i], "and", temp
        binmap[arr[i]] = 1

# driver program to check the above function
printPairs(A, len(A), n)
