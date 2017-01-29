'''
This program will find the longest substring without a repeating character

'''

def find_longest(astring = "abccdefgh"):
    if len(astring) < 2:
        return astring

    curr_start = 0
    maxlen = 1
    maxstart = 0
    maxend = 0
    dict1 = {}
    for index,char in enumerate(astring):
        if char in dict1:
            if dict1[char] >= curr_start:
                if maxlen < index - curr_start:
                    maxlen = index - curr_start
                    maxstart = curr_start
                    maxend = index-1
                curr_start = dict1[char] + 1
        dict1[char] = index

    if maxend < index-1:
        if maxlen < index - curr_start+1:
            maxend = index
            maxstart = curr_start

    return astring[maxstart:maxend+1]

bstring = 'abcdefgahijkblmnobpqr'
#bstring = "aaaaa"
print "longest substr is: " , find_longest(bstring)