'''
Write a function to get maximum consecutive sum of integers from an array.
'''

def max_sum_cons(arr):

    max_sum = 0
    curr_sum = 0
    for x in arr:
        curr_sum += x
        if curr_sum > max_sum:
            max_sum = curr_sum
        elif curr_sum < 0:
            curr_sum = 0

    return max_sum



arr1 = [1,2,3,4,5,20,-6,6,-30,50,4]
print "max sum is: ", max_sum_cons(arr1)
