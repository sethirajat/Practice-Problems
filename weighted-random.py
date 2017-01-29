'''
Question
Write a function that returns values randomly, according to their weight.
Let me give you an example. Suppose we have 3 elements with their weights: A (1), B (1) and C (2).
The function should return A with probability 25%, B with 25% and C with 50% based on the weights.
'''

from random import randint
import random

def return_random_weighted(Tuples):
    Arr = []

    for elem , weight in Tuples:
        Arr.extend([elem]*weight)

    num = randint(0,len(Arr)-1)

    return Arr[num]

def return_random_weighted2(Tuples):
    #Arr = []
    tot = 0
    for elem , weight in Tuples:
        #Arr.add(weight)
        tot += weight

    num = randint(1,tot)
    sum = 0
    curr_char = None
    index = 0
    while sum < num:
        curr_char,weight = Tuples[index]
        sum += weight
        index+=1


    return curr_char

def return_random_weighted3(Tuples):
    Arr = []
    tot = 0
    for elem , weight in Tuples:
        tot += weight
        Arr.append((elem,tot))


    num = randint(1,tot)
    curr_char = None
    left = 0
    right = len(Arr)-1

    while left <= right:
        mid = int((left+right)/2)
        if Arr[mid][1] == num or (Arr[mid][1] >= num and Arr[mid-1][1] < num):
            curr_char = Arr[mid][0]
            break
        if Arr[mid][1] > num:
            right = mid-1
        else:
            left = mid+1

    return curr_char


def return_random_weighted4(Tuples):
    #Arr = []
    tot = 0
    for elem , weight in Tuples:
        #Arr.add(weight)
        tot += weight

    prob = []
    for elem, weight in Tuples:
        prob.append(float(weight)/tot)
    num = random.random()
    sum = 0
    index = 0
    while sum < num and index < len(prob):
        sum += prob[index]
        index += 1


    return Tuples[index-1][0]


tup = [('A',1), ('B',1), ('C',2)]
dict1 = {'A':0, 'B':0, 'C':0}
for x in range(0,100):
    ret = return_random_weighted4(tup)
    dict1[ret] +=1
    print ret

print dict1