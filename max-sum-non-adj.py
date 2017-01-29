'''
Question
Given an array of integers, find a maximum sum of non-adjacent elements.
For example, inputs [1, 0, 3, 9, 2] should return 10 (1 + 9).
'''

def find_max_sum(Arr = [1, 0, 3, 9, 2]):
    if len(Arr) <= 2:
        return 0

    maxnum = Arr[0]
    maxsum = Arr[0]

    for num in range(2,len(Arr)):
        if Arr[num] + maxnum > maxsum:
            maxsum = Arr[num] + maxnum

        if maxnum < Arr[num-1]:
            maxnum = Arr[num-1]

    return maxsum


print find_max_sum([1,0,3,9,8,7])