def quicksort(l1):
    if len(l1) <= 1:
        return l1

    pivot = l1[-1]
    small = []
    large = []
    for index in range(len(l1)-1):
        if l1[index] <= pivot:
            small.append(l1[index])
        else:
            large.append(l1[index])

    return quicksort(small) + [pivot] + quicksort(large)





list1 = [5,10,6,3,2,4]

list2 = quicksort(list1)
print "sorted list is: ", list2