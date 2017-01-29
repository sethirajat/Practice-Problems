'''
find the length of a string without using len function and by using recursion
'''


def find_len(string1,index = 0):

    if string1 == "":
        return index

    return find_len(string1[index:],index+1)


def find_len1(string1,index = 0):

    try:
        x = string1[index]

    except IndexError:
        return index

    else:
        return find_len1(string1,index+1)



str1 = "Raj"

print "len of the string is: ", find_len(str1)
print "len of string using exception is: ", find_len1(str1)