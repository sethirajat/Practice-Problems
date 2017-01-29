'''
Program to implement stack and queue using a list in python
'''

class stack(object):

    def __init__(self):
        self.Array = []

    def push(self,val):
        self.Array.append(val)

    def pop(self):
        if len(self.Array) == 0:
            return None
        return self.Array.pop(len(self.Array)-1)

    def peek(self):
        if len(self.Array) == 0:
            return None
        return self.Array[-1]

class Queue(object):
    def __init__(self):
        self.Array = []

    def enqueue(self,val):
        self.Array.append(val)

    def dequeue(self):
        if len(self.Array) == 0:
            return None
        return self.Array.pop(0)

    def peek(self):
        if len(self.Array) == 0:
            return None
        return self.Array[0]


stack1 = stack()
queue1 = Queue()

stack1.push(5)
stack1.push(10)
stack1.push(15)
stack1.push(20)
print "peek at the stack at this point gives: ", stack1.peek()
print "pop at this time gives: ", stack1.pop()
print "peek after pop gives us: ", stack1.peek()
stack1.push(25)
stack1.push(30)
stack1.push(35)
stack1.push(40)
print "peek at the stack at end point gives: ", stack1.peek()
print "pop at this time gives: ", stack1.pop()
print "peek after pop gives us: ", stack1.peek()

queue1.enqueue(5)
queue1.enqueue(10)
queue1.enqueue(15)
queue1.enqueue(20)
print "peek at the queue at this point gives: ", queue1.peek()
print "dequeue at this time gives: ", queue1.dequeue()
print "peek after dequeue gives us: ", queue1.peek()
queue1.enqueue(25)
queue1.enqueue(30)
queue1.enqueue(35)
queue1.enqueue(40)
print "peek at the queue at end point gives: ", queue1.peek()
print "dequeue at this time gives: ", queue1.dequeue()
print "peek after dequeue gives us: ", queue1.peek()
