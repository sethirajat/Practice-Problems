#program to find the largest contiguous sum in an array

def findlargestsum(nums):

    #maxstartidx = 0
    #maxendidx = 0
    max_sum = 0
    curr_sum = 0
    #curr_startidx = 0
    #curr_endidx = 0

    for idx, num in enumerate(nums):
        curr_sum = curr_sum + num
        if curr_sum > max_sum:
            max_sum = curr_sum
            #maxstartidx = curr_startidx
            #maxendidx = idx
        elif curr_sum <= 0:
            curr_startidx = idx+1
            #curr_endidx = idx+1
            curr_sum = 0
        #else:
        #    curr_endidx = idx
    #print "start index is: ", maxstartidx
    #print "end index is: ", maxendidx
    print "maximum sum is:" , max_sum


inlist = []
inlist = [-2, 1, -3, 4, -1, 2, 1, -5, 4, 3, -3]

findlargestsum(inlist)
