'''
Write a function that divides two numbers without using the divide '/' operator.
'''

def divide(num, divisor):

    count = -1
    res = 0
    decimals = 0
    while num >0:
        num -= divisor
        count +=1
    if num == 0:
        return count
    else:
        res = count
        count = -1
        newnum = divisor + num
        decimals += 1
        newnum *= 10
        while newnum > 0:
            newnum -= divisor
            count += 1

        final_res = str(res) + "." + str(count)

        return final_res


numbr = int(raw_input("enter num"))
div = int(raw_input("enter divisor"))
print "result is: ", divide(numbr,div)
