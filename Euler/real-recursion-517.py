'''
Project Euler problem 517:
For every real number a>1a>1 is given the sequence gOfa by:
ga(x)=1ga(x)=1 for x < a
ga(x) = ga(x-1) + ga (x-a) for x >= a
G(n) = g(sqrt(n))(N)
G(90) = 7564511
find summation(G(p) for p prime and 10000000<p<10010000
'''

'''
THIS DOES NOT WORK YET
'''
import math

found_g = {}
def find_primes_and_call(start, stop):
    if start % 2 == 0:
        start += 1
    sum = 0
    while start < stop:
        root = math.sqrt(start)
        for x in range(3,int(root)):
            if start % x == 0:
                break
        else:
            sum += G(start, root)
        start += 2

    return sum % 1000000007

def G(num,root):
    return g(root,num)

def g(a,x):
    print "x is: ", x
    print "a is: ", a
    if x < a:
        return 1
    if (a,x) in found_g:
        return found_g[(a,x)]
    summ = g(a, x-1) + g(a, x-a)
    found_g[(a,x)] = summ
    return summ

start = 10000000
stop = 10010000
#print find_primes_and_call(start,stop)
print g(1,25)