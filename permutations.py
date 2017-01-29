'''
program to find all permutations of a string
'''

def find_perm(s1):
    if len(s1) <= 1:
        return s1
    result = []
    for index, char in enumerate(s1):
        restr = s1[:index] + s1[index+1:len(s1)]
        result += [char + x for x in find_perm(restr)]

    return result



instr = "abcd"
res = find_perm(instr)
print "size of result is: ", len(res)
print "results are: "
print res
print "size of result set is: ", len(set(res))
