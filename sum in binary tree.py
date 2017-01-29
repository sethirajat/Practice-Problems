'''
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
'''

class Node(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class Tree(object):
    def __init__(self,root):
        self.root = root

def root_to_leaf(root,sum):
    global sum_count
    if root == None:
        return
    if root.left == None and root.right == None:
        if root.val == sum:
            sum_count += 1

    else:
        if root.left is not None:
            root_to_leaf(root.left, sum - root.val)
        if root.right is not None:
            root_to_leaf(root.right, sum - root.val)

def root_to_leaf_dp(root,sum,curr_sum):
    global sum_count
    global global_dict
    if root == None:
        return
    if root.left in global_dict

    if root.left == None and root.right == None:
        if root.val == sum:
            sum_count += 1

    else:
        if root.left is not None:
            root_to_leaf(root.left, sum - root.val)
        if root.right is not None:
            root_to_leaf(root.right, sum - root.val)


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
sum_count = 0
root_to_leaf(node1,28)
global_dict = {}
print "total sum count found is: ", sum_count