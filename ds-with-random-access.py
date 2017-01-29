'''
We have to implement a data structure that should have insert, remove and GetRandom methods and all of them should work in constant time.
'''

'''
We will implement a mix of array and dict to make this possible
'''
from random import randint
class Myds(object):

    def __init__(self):
        self.dict = {}
        self.arr = []

    def insert(self,val):
        if val in self.dict:
            return False
        self.arr.append(val)
        self.dict[val] = len(self.arr)- 1
            return True

    def remove(self,val):
        if val not in self.dict:
            return False
        idx = self.dict[val]
        last = self.arr[-1]
        self.arr[idx], self.arr[-1] = self.arr[-1], self.arr[idx]
        self.dict[last] = idx
        self.dict.pop(val)
        self.arr.pop()
        return True

    def get_random(self):
        keylen = len(self.arr)
        if keylen < 1:
            return False
        rand = randint(0,keylen-1)
        return self.arr[rand]

    def get_all(self):
        return self.arr


myobj1 = Myds()

myobj1.insert(1)
myobj1.insert(2)
myobj1.insert(3)
myobj1.insert(4)
myobj1.insert(5)
myobj1.insert(6)

print "current elements: "
print myobj1.get_all()

myobj1.remove(3)
myobj1.remove(4)
print "current elements after deletion: "
print myobj1.get_all()

dict_count = {1:0, 2:0, 5:0, 6:0}
for x in range(100):
    rnd = myobj1.get_random()
    dict_count[rnd] += 1

print "random results: "
print dict_count