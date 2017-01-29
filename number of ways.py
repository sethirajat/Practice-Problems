dict1 = {}
call_count = 0
def return_ways(Arr,idx,num,curr):
    #Assuming the array a is sorted in descending order
    global call_count
    #call_count += 1
    if idx >= len(Arr):
        return 0
    global dict1
    if (idx,num-curr) in dict1:
        return dict1[(idx,num-curr)]

    count = 0

    sum = curr
    ind = 0
    length = len(Arr)
    while sum < num:
        call_count += 1
        sum = curr + ind*Arr[idx]
        if sum == num:
            count+=1
            continue
        if idx < length-1:
            count += return_ways(Arr,idx+1,num,sum)
        ind += 1
    dict1[(idx,num-curr)] = count
    return count


arr = [25,10,5,1]
nm = 100

count = return_ways(arr,0,nm,0)

print "the count is: ", count
print "the call count is: ", call_count