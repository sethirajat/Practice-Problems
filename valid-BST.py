import sys

def isvalidBST(root, minimum = -sys.maxint, maximum = sys.maxint):
    assert (root is not None)

    if root.val < minimum or root.val > maximum:
        return False
    leftres = True
    rightres = True
    if root.left is not None:
        leftres = isvalidBST(root.left, minimum, root.val)

    if root.right is not None:
        rightres = isvalidBST(root.right, root.val, maximum)

    return leftres and rightres


class node(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

root = node(6)
if isvalidBST(root):
    print "success"


