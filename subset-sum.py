'''
Objective: Given a set of positive integers, and a value sum S, find out if there exist a subset in array whose sum is equal to given sum S.

Example:

int[] A = { 3, 2, 7, 1}, S = 6

Output: True, subset is (3, 2, 1}
'''

def subset_sum(arr,S, res = [], idx=0):
    global call_count
    call_count +=1
    if len(arr) <= idx:
        return
    global dict_with,dict_without
    if sum(res) + arr[idx] == S:
        res1 = []
        res1 = res + [arr[idx]]
        print "subset found: ", res1

    subset_sum(arr,S,res[:],idx+1)
    res.append(arr[idx])
    subset_sum(arr,S,res[:],idx+1)

call_count = 0
arr = [ 3, 2, 7, 1]
SS = 6
dict_with = {}
dict_without = {}
subset_sum(arr,SS)
print "the total calls count is: ", call_count



