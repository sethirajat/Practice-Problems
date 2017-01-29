'''
Given two strings str1 and str2, find if str1 is a subsequence of str2.
A subsequence is a sequence that can be derived from another sequence by deleting
some elements without changing the order of the remaining elements (source: wiki).
Expected time complexity is linear.
'''

def find_subseq(str1,str2):
    lens1 = len(str1)
    lens2 = len(str2)
    if lens2 < lens1:
        return False

    currents2 = 0
    currents1 = 0
    while currents1 < lens1 and currents2 < lens2 and lens1-currents1 <= lens2-currents2:
        if str2[currents2] == str1[currents1]:
            currents1 += 1
        currents2 += 1

    if currents1 == lens1:
        return True
    else:
        return False


str1 = "AXC"
str2 = "ADXCPY"
if find_subseq(str1,str2):
    print "yes, it is a subsequence"
else:
    print "no, not a subseq"

