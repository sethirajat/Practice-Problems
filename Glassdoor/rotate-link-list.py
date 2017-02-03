'''
rotate a link-list clock/anti-clock wise by n
'''

class node(object):
    def __init__(self, val = None,next = None):
        self.val = val
        self.next = next


class link_list(object):
    def __init__(self,head=None):
        self.head = head

    def rotate_clock(self,n):

        if self.head is None:
            raise ValueError("head is not present")

        length = self.find_len(self.head)
        to_move = length - (n%length)
        current = self.head
        prev = None
        while to_move > 0:
            prev = current
            current = current.next
            to_move -= 1


        newhead = current
        while current.next is not None:
            current = current.next

        current.next = self.head
        prev.next = None
        self.head = newhead

    def rotate_anti_clock(self,n):

        if self.head is None:
            raise ValueError("head is not present")

        length = self.find_len(self.head)
        to_move = (n%length)
        current = self.head
        prev = None
        while to_move > 0:
            prev = current
            current = current.next
            to_move -= 1


        newhead = current
        while current.next is not None:
            current = current.next

        current.next = self.head
        prev.next = None
        self.head = newhead

    def find_len(self,head):
        count = 0
        current = head
        while current is not None:
            count += 1
            current = current.next

        return count

    def print_all(self):
        current = self.head
        final_str = ""
        while current is not None:
            final_str += str(current.val) + "-->"
            current = current.next

        final_str += "None"
        print final_str


firstnode = node(1)
prevnode = firstnode

for x in range(4):
    newnode = node(x+2)
    prevnode.next = newnode
    prevnode = prevnode.next

newlist = link_list(head=firstnode)
newlist.print_all()
newlist.rotate_clock(3)
newlist.print_all()
newlist.rotate_anti_clock(3)
newlist.print_all()







