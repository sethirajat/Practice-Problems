'''
Given the daily values of a stock, find how you can lose the most with one buy-sell trading
'''

def find_max_loss(arr):

    #maxim = arr[0]
    cur_max = arr[0]
    maxloss = float('-inf')
    #curlos = 0
    #minim = arr[1]+1

    for x in range(1,len(arr)):
        if cur_max - arr[x] > maxloss:
            #maxim = cur_max
            #minim = arr[x]
            maxloss = cur_max - arr[x]
        if arr[x] > cur_max:
            cur_max = arr[x]


    return maxloss

arr = [11,20,24,51,10,99,15,1,199,130]
arr1 = [100,130,200,240,510,1000,9900,15000,111000]
print "loss for arr is: ", find_max_loss(arr)

