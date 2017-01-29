import Queue
'''
arr = [0,1,2,3,4,5,6,7,8]
pivot = int(raw_input("enter pivot\n"))
print "first half: ", arr[:pivot]
print "second half: ", arr[pivot:]

s1 = "abcd"
num = int(raw_input("enter no"))
s2 = s1[:num]
s3 = s1[num+1:]

print "s2 is: ", s2
print "s3 is: ", s3
'''
'''
char = 'c'
list1 = ["bc","cd","db"]
list2 = []
list2 += [char + x for x in list1]
print "list2 is: "
print list2

def find_perms(s1):
    if len(s1) <= 1:
        return s1

    result = []

    for index, char in enumerate(s1):
        newchr = s1[:index] + s1[index+1:]
        result += [char + x for x in find_perms(newchr)]

    return result


instr = "abcd"
res = find_perms(instr)
print "size of result is: ", len(res)
print "results are: "
print res
print "size of result set is: ", len(set(res))


list1 = [0]*10
list1.insert(6,100)
#list1[0] = 100

print len(list1)
print list1

q1 = Queue.deque()
q2 = Queue.Queue()
q3 = Queue.LifoQueue()
q4 = Queue.PriorityQueue()

q1.append(5)
q2.put(5)
q3.put(5)
q4.put(5)
q1.append(3)
q2.put(3)
q3.put(3)
q4.put(3)
q1.append(8)
q2.put(8)
q3.put(8)
q4.put(8)

print "q1:", q1.pop()
print "q2:", q2.get()
print "q3:", q3.get()
print "q4:", q4.get()

a = "a"
b = "b"
print "a is: ", a
print "b is: ", b
a,b = b,a
print "a is: ", a
print "b is: ", b

for i in range(3,-1,-1):
    print i

for j in range(3,0,-1):
    print "j is: ", j
'''

inf = float('inf')
A = [[0,1,4,inf,3],
     [1,0,2,inf,4],
     [4,2,0,1,5],
     [inf,inf,1,0,3],
     [3,4,5,3,0]]

for row in A:
    print row

num = 4
for row in A:
    for val in row:
        print '{:4}'.format(val),
    print


import matrix

mat1 = matrix.Matrix(4,5)
mat1.printMatrix()
mat1.set(1,2,'a')
mat1.printMatrix()

list1 = [1,2,3]
list2 = [4,5,6]

print "adding is: ", list1+list2
list1.append(list2)
print "appending is: ", list1
list2.extend(list1)
print "extending is: ", list2

dict1 = {}
dict1[10] = "dus"
if 10 in dict1:
    print "this is before none"
dict1[20] = "bees"
dict1.pop(10)
if 10 in dict1:
    print "this is after none"


Ar = [5]
br = Ar[1:]
cr = Ar[0]

start = 2
end = 10
for x in range(start,end):
    print "x is: ", x

test1 = 5
for num in range(2,101):
    for i in range(2,num):
        if num%i == 0:
            break
    else:
        print num
    test1 -=1

Ar = [0,1,2,3,4,5]
print "third element is: ", Ar[2]
print "4th element is: ", Ar[3]
Ar.pop(2)
print "third element after deletion is: ", Ar[2]
print "4th element is: ", Ar[3]

list123 = ["1", "2"]
abc, cde = list123
print "abc and cde are: ", abc , "   ", cde


bin(-18)