#print bin(-18)
'''
program for in order traversal iteratively
'''

class Node:
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorder_iter(root):

    if root is None:
        return None

    stack = []
    current = root

    while True:
        if current is not None:
            stack.append(current)
            current = current.left

        else:
            if len(stack) == 0:
                break
            current = stack.pop()
            print current.data
            current = current.right


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

inorder_iter(root)

print 5&-5
print bin(5)
print bin(-5)