'''
find the pairs of numbers in a 2d array. You can use one position only once
'''

def find_pairs(array):

    row = len(array)
    cols = len(array[0])

    if row == 0:
        return

    result = []
    found = {}

    for x in range(row):
        for y in range(cols):
            elem = array[x][y]
            if elem in found:
                result.append([(x,y),found[elem]])
                found.pop(elem)

            else:
                found[elem] = (x,y)

    return result

arr = [[1,3,4,1],[6,1,7,8], [9,0,5,8],[2,2,1,2]]
print "result from find pairs: "
print find_pairs(arr)