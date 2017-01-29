'''
How to find the deepest node in a tree.
'''


class Node(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class Tree(object):
    def __init__(self,root):
        self.root = root


def find_deepest(root):

    global max_heights
    global call_count
    call_count += 1
    if root in max_heights:
       return max_heights[root]
    if root.left == None and root.right == None:
        max_heights[root] = [root,1]
        return [root,1]
    left_h, right_h = [None,0],[None,0]

    if root.left is not None:
        left_h = find_deepest(root.left)

    if root.right is not None:
        right_h = find_deepest(root.right)

    if left_h[1] >= right_h[1]:
        left_h[1] += 1
        max_heights[root] = left_h
        return left_h
    else:
        right_h[1] += 1
        max_heights[root] = right_h
        return right_h


def find_deepest_bfs(root):
    queue = []
    queue.append([root,0])
    deepest = root
    max_height = 0
    global call_count

    while queue:
        call_count +=1
        element = queue.pop(0)
        print "the node retrieved is: ", element[0].val
        height = element[1]
        if height > max_height:
            deepest = element[0]
            max_height = height
        if element[0].left is not None:
            queue.append([element[0].left,height+1])
        if element[0].right is not None:
            queue.append([element[0].right,height+1])

    return [deepest,max_height]

max_height = 0
max_elem = None
def find_deepest_nw(root,h = -1):
    global max_height,max_elem
    if root is None:
        return

    height = h+1
    if height > max_height:
        max_height = height
        max_elem = root

    if root.left is not None:
        find_deepest_nw(root.left,height)

    if root.right is not None:
        find_deepest_nw(root.right,height)

max_heights = {}
call_count = 0
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node8 = Node(8)
node9 = Node(9)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7
node7.left = node8
node8.right = node9

tree1 = Tree(node1)
print "the deepest node and it's height is: "
#result = find_deepest(tree1.root)
result = find_deepest_bfs(tree1.root)
print result[0].val, result[1]
print "the total calls are: ", call_count
print "result from new: "
find_deepest_nw(tree1.root)
print max_elem.val
print "max height is: ", max_height


class Thing(object):
    x = 1
something = Thing()
print something.x
something.y = something.x
print something.y
print something