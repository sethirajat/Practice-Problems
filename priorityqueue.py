'''
implement your own priority queue
'''

class pqueue(object):

    def __init__(self):
        self.elements = []

    def insert(self,val):
        self.elements.append(val)
        if len(self.elements) == 1:
            return

        child = len(self.elements)-1
        parent = int((child -1)/2)
        while parent >= 0 and self.elements[child] < self.elements[parent]:
            self.elements[child], self.elements[parent] = self.elements[parent], self.elements[child]
            child = parent
            parent = int((child -1)/2)

        print "print after insertion: "
        self.print_all()
        return

    def remove(self):
        if len(self.elements) < 1:
            return -1
        if len(self.elements) < 3:
            elem = self.elements.pop(0)
            return elem

        res = self.elements[0]
        self.elements[0], self.elements[len(self.elements)-1] = self.elements[len(self.elements)-1],self.elements[0]
        self.elements.pop()
        parent = 0
        leftchild = 1
        rightchild = 2
        while leftchild <= len(self.elements)-1:
            minchild = leftchild
            if rightchild <= len(self.elements)-1 and self.elements[rightchild] < self.elements[leftchild]:
                minchild = rightchild
            if self.elements[parent] > self.elements[minchild]:
                self.elements[parent], self.elements[minchild] = self.elements[minchild], self.elements[parent]
                parent = minchild
                leftchild = parent *2 +1
                rightchild = parent *2 + 2
            else:
                break

        return res

    def print_all(self):
        print "all elements: "
        print self.elements

pq1 = pqueue()
pq1.insert(10)
pq1.insert(74)
pq1.insert(32)
pq1.insert(76)
pq1.insert(89)
pq1.insert(39)
pq1.insert(29)
pq1.insert(18)
pq1.insert(20)
pq1.insert(28)
pq1.insert(37)
pq1.insert(26)
pq1.print_all()
remvd = pq1.remove()
print "removed elem: ", remvd
pq1.print_all()
remvd = pq1.remove()
print "removed elem: ", remvd
pq1.print_all()