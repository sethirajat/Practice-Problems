'''
program to find sum of a binary tree
'''

class node(object):
    def __init__(self, val=None,right = None, left = None):
        self.val = val
        self.left = left
        self.right = right

class bin_tree(object):
    def __init__(self, root = None):
        self.root = root

    def sums(self):
        if self.root is None:
            return 0

        return self.sum_recur(self.root)

    def sum_recur(self,root):
        if root is None:
            return 0

        left_sum = 0
        if root.left is not None:
            left_sum = self.sum_recur(root.left)
        right_sum = 0
        if root.right is not None:
            right_sum = self.sum_recur(root.right)

        return root.val + left_sum + right_sum


