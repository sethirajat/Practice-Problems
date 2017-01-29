'''
Max-Heap sort using a list
'''



def max_heapify(arr,n,i):
    left = 2 *i + 1
    right = 2 *i + 2
    largest = i
    if left < n and arr[left] > arr[i]:
        largest = left

    if right < n and arr[right] > arr[i]:
        largest = right

    if largest != i:
        arr[i],arr[largest] = arr[largest], arr[i]
        max_heapify(arr,n,largest)


def heapsort(arr):

    arr_len = len(arr)
    for x in range(arr_len):
        max_heapify(arr,arr_len,0) #this 0 should be replaced with x ?

# Driver code to test above
arr = [10, 11, 13, 5, 6, 7]
heapsort(arr)
n = len(arr)
print ("Sorted array is")
for i in range(n):
    print ("%d" % arr[i])


