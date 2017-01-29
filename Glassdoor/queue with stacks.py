
class Queue(object):
    def __init__(self):
        self.instack = []
        self.outstack = []

    def enqueue_back(self,val):
        self.instack.append(val)

    def enqueue_front(self,val):
        self.outstack.append(val)

    def dequeue_front(self):
        if len(self.outstack) == 0:
            while len(self.instack)> 0:
                self.outstack.append(self.instack.pop())

        if len(self.outstack) > 0:
            return self.outstack.pop()
        else:
            raise ValueError("No elements in the queue")

    def dequeue_back(self):
        if len(self.instack) == 0:
            while len(self.outstack) > 0:
                self.instack.append(self.outstack.pop())

        if len(self.instack) > 0:
            return self.instack.pop()
        else:
            raise ValueError("no elements yo")



queue1 = Queue()
queue1.enqueue_back(1)
queue1.enqueue_back(2)
queue1.enqueue_back(3)
queue1.enqueue_back(4)
queue1.enqueue_back(5)
queue1.enqueue_back(6)

print queue1.dequeue_front()
queue1.enqueue_front(7)
print queue1.dequeue_front()
print queue1.dequeue_front()
print queue1.dequeue_back()
queue1.enqueue_back(8)
for x in range(20):
    try:
        print queue1.dequeue_front()
        print queue1.dequeue_back()
    except ValueError,e:
        print e.message
        break

