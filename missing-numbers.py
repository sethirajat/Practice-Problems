'''
You are given an array with distinct numbers between 1 to 100. You have to return a string which says the number's range
which are not in the given array separated by comma.

Eg:
Input: [50,75]

Output: (0-49,51-74,76-100)
'''

def find_missing(arr):
    if len(arr) == 0:
        return "0-100"

    res = []
    start = -1
    end = -1
    started = False
    idx = 0
    for x in range(101):
        if x != arr[idx]:
            if started:
                end += 1
            else:
                start = end = x
                started = True
        else:
            if started:
                entry = (start,end)
                res.append(entry)
                started = False
            start = x + 1
            idx+= 1
            if idx >= len(arr):
                end = 100
                if start <= 100:
                    entry = (start,end)
                    res.append(entry)
                break


    res_string = ",".join(str(entry[0]) + "-" + str(entry[1]) for entry in res)

    return res_string

arr = [50,75,99]
print find_missing(arr)
