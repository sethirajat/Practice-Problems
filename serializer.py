'''
Given a list of words, develop two functions to serialize and deserialize into a single string.
Given a string in the format: 2(abc)4(df), write a function to decompress the string to the following format: abcabcdfdfdfdf

'''
DELIMITER = "&"
def serialize(arr):

    global DELIMITER
    maxlen = 0
    result_str = ""
    temp_str = ""
    for string in arr:
        curr_len = len(string)
        result_str += str(curr_len) + ","
        temp_str += string
        if curr_len > maxlen:
            maxlen = curr_len

    result_str += DELIMITER + temp_str
    return result_str

def getnextnum(start,string,delim):
    nxtsize = 0
    strt_idx = start
    while strt_idx < len(string):
        if string[strt_idx] == delim:
            break
        nxtsize += 1
        strt_idx += 1

    res = int(string[start:strt_idx])
    return res,nxtsize

def deserialize(string):
    result = []
    for index in range(len(string)):
        if string[index] == DELIMITER:
            break

    start_idx = index+1
    start_num = 0
    while start_idx < len(string) and start_num < index:
        nextnum,nxtsize = getnextnum(start_num,string,',')
        result.append(string[start_idx:start_idx+nextnum])
        start_idx += nextnum
        start_num += nxtsize+1

    return result
def getnextstr(start,string,delim):
    res = ""
    idx = start
    while idx < len(string):
        if string[idx] == delim:
            break
        res += string[idx]
        idx += 1

    return res

def decompress(string):

    res = ""
    #curr_num = 0
    index = 0
    while index < len(string):
        nextnum,nxtsize = getnextnum(index,string,'(')
        nextstr = getnextstr(index+nxtsize+1,string,')')
        res += nextstr*nextnum
        index += nxtsize + 2 + len(nextstr)

    return res




some_unicode_strings = []
some_unicode_strings.append("gnrales okie dokie")
some_unicode_strings.append("555 okie dokie;")
serialized = serialize(some_unicode_strings)
print serialized
deserialized = deserialize(serialized)
for blob in deserialized:
    print blob

s1 = "2(abc)4(df)"
print decompress(s1)

