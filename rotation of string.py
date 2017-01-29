'''
Assume you have a method isSubstring which checks if one word is a substring of another.
Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to
isSubstring (i.e., "waterbottle" is a rotation of "erbottlewat").
Note: we will write the isSubstring method as well
'''

def isSubstring (mainstring, substring):
    mainlen = len(mainstring)
    sublen = len(substring)
    if mainlen < sublen:
        return False

    start = 0
    end = sublen

    while end <= mainlen:
        if mainstring[start:end] == substring:
            return True
        start +=1
        end +=1

    return False

#test issubstring
'''
str1 = "godisgreat"
str2 = "eat"

if isSubstring(str1,str2):
    print "yes, it is a substring"
else:
    print "no, not a substring"
'''

def find_rotation(s1,s2):
    if len(s1) != len(s2):
        return False

    s3 = s1 + s1
    if isSubstring(s3,s2):
        return True
    else:
        return False



str1 = "waterbottle"
str2 = "erbottlewat"

if find_rotation(str1,str2):
    print "yes, it is a rotation"
else:
    print "no, not a rotation"
