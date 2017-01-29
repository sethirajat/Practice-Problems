import Queue
import heapq


def find_smallest_k():
    starqueue = Queue.PriorityQueue(3)
    starheap = []
    stars = open('stars.txt', 'r')
    n = 3
    for star in stars:
        name, dist = star.split(',')
        entry = (int(dist.strip()), name)
        if n:
            heapq.heappush(starheap, entry)
            n -= 1
            continue
        if entry[0] > starheap[0][0]:
            heapq.heapreplace(starheap,entry)

    print "finally: "
    print starheap
    #for x in range(starqueue.qsize()):
    #    print starqueue.get()

    stars.close()



def funnel(n, numbers):
    if n == 0: return []
    heap = numbers[:n]
    heapq.heapify(heap)
    for k in numbers[n:]:
        if heap[0] < k:
            heapq.heapreplace(heap, k)
    return heap


class heap(object):

    def __init__(self,maxsize = 1000):
        self.heap = []
        self.count = 0
        self.maxsize = maxsize

    def push(self,val):
        if self.count >= self.maxsize:
            return IndexError

        self.heap.append(val)
        self.shiftup()

    def shiftup(self):
        child = len(self.heap)-1
        parent = int((child-1)/2)

        while parent >= 0:
            if self.heap[parent] < self.heap[child]:
                self.heap[parent] , self.heap[child] = self.heap[child] , self.heap[parent]
                child = parent
                parent = int((child-1)/2)
            else:
                break
    def shiftdown(self,pos):
        parent = pos
        lchild = parent*2 +1
        rchild = parent*2 +2

        while lchild < len(self.heap):
            larger = lchild
            if rchild < len(self.heap) and self.heap[rchild] > self.heap[lchild]:
                larger = rchild

            if self.heap[parent] < self.heap[larger]:
                self.heap[parent], self.heap[larger] = self.heap[larger], self.heap[parent]
                parent = larger
                lchild = parent * 2 + 1
                rchild = parent * 2 + 2
            else:
                break

    def replace(self,val):
        if len(self.heap) == 0:
            return IndexError

        self.heap[0] = val
        self.shiftdown(0)

def smallest_own():
    heap1 = heap()
    stars = open('stars.txt', 'r')
    n = 3
    for star in stars:
        name, dist = star.split(',')
        entry = (int(dist.strip()), name)
        if n:
            heap1.push(entry[0])
            n -= 1
            continue
        if entry[0] < heap1.heap[0]:
            heap1.replace(entry[0])

    print "finally: "
    print heap1.heap




smallest_own()

#find_smallest_k()