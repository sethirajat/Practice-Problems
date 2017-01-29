count = 0
def return_ways(num,idx):
    #Assuming the array a is sorted in descending order
    global count
    if len(idx:len[Arr]) < 1:
        return


    if(num < 0) :
         return

    #ind = 0
    length = len(Arr)
    sum = 0
    while sum <= num:

        if(sum == num) :
            count +=1
            return

        if length > 1:
            return_ways(Arr[1:],num-sum)

        sum  = sum + Arr[0]
    return


arr = [25,10,5,1]
nm = 100

return_ways(arr,nm)

print "the count is: ", count