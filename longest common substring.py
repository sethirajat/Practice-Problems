import matrix
def LCS(s1, s2):
    m = len(s1)
    n = len(s2)

    mat1 = matrix.Matrix(m,n)
    res = 0

    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0:
                num = 0
            else:
                num = mat1.get(i-1,j-1)
            if s1[i] == s2[j]:
                mat1.set(i,j,num+1)
                res = max(res,num+1)
            else:
                mat1.set(i,j,0)
            mat1.printMatrix()



    mat1.printMatrix()
    print "result is: ", res

def find_len(s1,s2,x,y):
    m = len(s1)
    n = len(s2)
    count = 0
    while x < m and y < n:
        if s1[x] == s2[y]:
            count += 1
            x += 1
            y += 1
        else:
            break
    return count

def LCS2(s1,s2):
    m = len(s1)
    n = len(s2)
    res = 0
    for x in range(m):
        for y in range(n):
            if s1[x] == s2[y]:
                curr_len = find_len(s1,s2,x,y)
                res = max(curr_len,res)

    print "result brute is: ", res
    return res



s1 = "GeeksforGeeks"
s2 = "malunGeeks"

LCS(s1,s2)
LCS2(s1,s2)