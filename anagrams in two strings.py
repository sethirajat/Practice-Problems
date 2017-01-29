'''
Check if one string contains an anagram of the other string
'''
import string
import math
def map_chars_to_prime():
    dict_prime = {}
    chars = list(string.ascii_lowercase)
    charidx = 0
    for num in range (3,201,2):
        for div in range (2,int(math.sqrt(num))+1):
            if num%div == 0:
                break
        else:
            dict_prime[chars[charidx]] = num
            charidx += 1
        if charidx > 25:
            break
    return dict_prime




#we have to find if string1 contains an anagram of string2
def check_anagram(string1,string2):
    if string1 is None or string2 is None:
        raise Exception("bad arguments")

    len1 = len(string1)
    len2 = len(string2)

    if len1 < len2:
        raise Exception("bad argument size")

    dict1 = map_chars_to_prime()
    hash2 = 1
    for char in string2:
        hash2 *= dict1[char]

    start = 0
    end = len2
    hash1 = 1
    for char in string1[:end]:
        hash1 *= dict1[char]
    if hash1 == hash2:
        return True
    while end < len1:
        hash1 /= dict1[string1[start]]
        hash1 *= dict1[string1[end]]
        if hash1 == hash2:
            return True
        start += 1
        end += 1

    return False

str1 = "dog"
str2 = "godisgreatgdd"

if check_anagram(str2,str1):
    print "yes anagrams"
else:
    print "no ana gram baby"

