'''
This program is to convert a given arraty of positive and negative integers into zigzag. That is one max followed by one min element.

'''

def WiggleArrangeArray(intArr):
    return WiggleArrangeArray1(intArr)
    if len(intArr) < 2:
        return intArr

    sortedArr = sorted(intArr)
    start = 0
    end = len(sortedArr)-1
    zigzagArr = []
    while start < end:
        zigzagArr.append(sortedArr[end])
        end-=1
        zigzagArr.append(sortedArr[start])
        start+=1

    if len(sortedArr)%2 != 0:
        zigzagArr.append(sortedArr[start])

    return zigzagArr
#def WiggleArrangeArray1(arr):
#    pass

def Merge_regular(first, second):
    first_length = len(first)
    second_length = len(second)

    i,j = 0,0
    sortedArr = []
    while i < first_length and j < second_length:
        if first[i] <= second[j]:
            sortedArr.append(first[i])
            i+= 1
        else:
            sortedArr.append(second[j])
            j+=1

    while i < first_length:
        sortedArr.append(first[i])
        i+=1
    while j < second_length:
        sortedArr.append(second[j])
        j+=1

    return sortedArr


def Merge_sort(intArr):
    if len(intArr)<= 1:
        return intArr

    mid = int(len(intArr) / 2)
    first_half = Merge_sort(intArr[:mid])
    second_half = Merge_sort(intArr[mid:])
    return Merge_regular(first_half,second_half)

def Merge_zigzag(first,second):
    first_end = len(first)-1
    second_end = len(second)-1
    first_start, second_start = 0,0
    zigzag = []

    while first_start <= first_end and second_start <= second_end:
        if first[first_end] < second[second_end]:
            zigzag.append(second[second_end])
            second_end-=1
        else:
            zigzag.append(first[first_end])
            first_end-=1

        if first[first_start] < second[second_start]:
            zigzag.append(first[first_start])
            first_start+=1
        else:
            zigzag.append(second[second_start])
            second_start+=1

    while first_start <= first_end:
        zigzag.append(first[first_end])
        if first_start != first_end:
            zigzag.append(first[first_start])
            first_start+=1
        first_end-=1

    while second_start <= second_end:
        zigzag.append(second[second_end])
        if second_start != second_end:
            zigzag.append(second[second_start])
            second_start+=1
        second_end-=1

    return zigzag



def WiggleArrangeArray1(intArr):
    if len(intArr) < 2:
        return intArr

    mid = int(len(intArr)/2)
    first_half = Merge_sort(intArr[:mid])

    second_half = Merge_sort(intArr[mid:])
    print "first half is: ", first_half
    print "second half is: ", second_half

    return Merge_zigzag(first_half,second_half)


#Below code is just for testing purpose
arr = [5,2,7,8,-2,25,25]
print "the result is: "
print WiggleArrangeArray(arr)

arr1 = [-27676,211621,904304,161270,-292822,732004,860511,-825806,-721722,536428,-927571,-287004]
print "second value is: "
print WiggleArrangeArray(arr1)

#if __name__== "__main__":
#    main()


