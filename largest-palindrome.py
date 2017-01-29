


def find_palin(s1, loc, start_loc):
    left = loc
    right = start_loc
    delta = 0
    if left == right:
        delta = -1
    slen = len(s1)
    pal_len = 0
    while left >=0 and right <slen:
        if s1[left] == s1[right]:
            pal_len += 2
            left -= 1
            right += 1
        else:
            break

    return pal_len + delta


def find_largest_palin(s2):
    slen = len(s2)
    if slen <= 1:
        return slen

    highest_len = 0
    for index in range(slen):
        curr_len = find_palin(s2,index,index)
        if curr_len > highest_len:
            highest_len = curr_len
        curr_len = find_palin(s2,index,index+1)
        if curr_len > highest_len:
            highest_len = curr_len

    return highest_len


instring = raw_input("enter the string\n")
pal_len = find_largest_palin(instring)
print "Highest length is: ", pal_len




