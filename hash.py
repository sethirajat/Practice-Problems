'''
program to write your own hash table.
'''

class kvp(object):

    def __init__(self,key = None, val = None):
        self.key = key
        self.value = val


    def getkey(self):
        return self.key

    def getvalue(self):
        return self.value

    def insert_kv(self,key,val):
        self.key = key
        self.value = val



class hash_table(object):
    def __init__(self,size):

        self.size = self.find_nearest_prime(size)
        self.table = [kvp() for _ in xrange(self.size)]

    def find_nearest_prime(self,sz):
        isprime = False
        size = sz
        while not isprime:
            if size%2 > 0 and size%3 >0 and size%5 >0 and size%7 > 0:
                isprime = True
                break
            size+=1
        return size
    #Check if key is invalid or zero
    #check if table is full
    def insert_val(self,key,val):
        hash = key%self.size
        existing_key = self.table[hash].getkey()
        for x in range(self.size):
            hash = (hash +1)%self.size
            existing_key = self.table[hash].getkey()
            if existing_key is None:
                break
        if existing_key is not None:
            raise Exception("table full")
        self.table[hash].insert_kv(key,val)


    def getval(self,key):
        hash = key%self.size
        if self.table[hash].getkey() == key:
            return self.table[hash].getvalue()
        for x in range(self.size):
            hash = (hash+1)%self.size
            if self.table[hash].getkey() == key:
                return self.table[hash].getvalue()

        return None



hasht = hash_table(100)
hasht.insert_val(1000,"hazaar")
hasht.insert_val(2000,"do hazaar")
hasht.insert_val(3000,"teen hazaar")
hasht.insert_val(4000,"chaar hazaar")
hasht.insert_val(5000,"panch hazaar")
hasht.insert_val(6000,"chhe hazaar")
base = 1000
for x in range(110):
    hasht.insert_val(base+x,"jo bhi hai")
    print "inserted: ", x
print hasht.getval(1000)
print hasht.getval(6000)
print hasht.getval(3000)
print "this one is for 7000: "
if hasht.getval(7000) is None:
    print "yes none"
else:
    print "lag gye l"