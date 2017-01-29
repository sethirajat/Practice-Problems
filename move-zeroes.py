'''
Question
Modify the array by moving all the zeros to the end(right side). The order of other  elements doesn't matter.
Let's have an example. For array [1, 2, 0, 3, 0, 1, 2], the program can output [1, 2, 3, 1, 2, 0, 0].

'''

def move_zeroes(Arr =[1, 2, 0, 3, 0, 1, 2] ):
    if len(Arr) <= 1 :
        return Arr

    last = len(Arr)-1
    left = 0

    while last > left and Arr[last] == 0:
        last -= 1

    while left < last:
        if Arr[left] == 0:
            Arr[left], Arr[last] = Arr[last],Arr[left]

        left +=1
        while last > left and Arr[last] == 0:
            last -= 1

    return Arr


print move_zeroes([0,1, 2, 0, 3, 0, 1, 2, 0] )