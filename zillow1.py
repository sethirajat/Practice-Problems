def parse_long(s):

    if s is None or len(s) == 0:
        raise Exception('Invalid string')

    result = 0
    power_10 = 1
    last_char = -1
    if s[0] == '-':
        last_char = 0
        power_10 = -1

    for i in range(len(s) - 1, last_char, -1):
        current_val = ord(s[i]) - ord('0')
        #print "current val: ", current_val
        if current_val < 0 or current_val > 9:
            raise Exception('Invalid string')
        result = result + current_val*power_10
        #print "result at this point is: ", result
        power_10 *= 10


    return result


in_string = raw_input("enter the string\n")
retVal = parse_long(in_string)
print "the value is: ", retVal