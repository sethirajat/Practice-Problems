class Node(object):  # Please do not remove or rename any of this code
    """Represents a single node in the Ternary Search Tree"""

    def __init__(self, val):
        self.val = val
        self.left = None
        self.mid = None
        self.right = None


class Tree(object):  # Please do not remove or rename any of this code
    """The Ternary Search Tree"""

    def __init__(self):
        self.root = None

    # Please complete this method.
    """Inserts val into the tree. There is no need to rebalance the tree."""

    def insert(self, val):
        newnode = Node(val)

        if self.root is None:
            self.root = newnode
            return

        child = self.root
        parent = child
        while child is not None:
            parent = child
            if val < child.val:
                child = child.left
            elif val > child.val:
                child = child.right
            else:
                child = child.mid

        if val < parent.val:
            parent.left = newnode
        elif val > parent.val:
            parent.right = newnode
        else:
            parent.mid = newnode



    # Please complete this method.

    """Deletes only one instance of val from the tree.
       If val does not exist in the tree, do nothing.
       There is no need to rebalance the tree."""

    def delete(self, val):

        if self.root is None:
            return
        deleteRoot = False
        if val == self.root.val:
            deleteRoot = True

        temp = self.root
        parent = None
        while temp is not None:
            if val == temp.val:
                break
            parent = temp
            if val < temp.val:
                temp = temp.left
            else:
                temp = temp.right

        if temp is None:
            return
        if parent is None:
            self.root = self.delete_at(temp)
            return
        if parent.val < temp.val:
            parent.right = self.delete_at(temp)
        else:
            parent.right = self.delete_at(temp)

    def delete_at(self, delnode):
        if delnode.mid is not None:
            delnode.mid = None
            return delnode

        if delnode.left is None:
            if delnode.right is None:
                return None
            else:
                return delnode.right
        if delnode.right is None:
            return delnode.left

        newdelnode = self.find_max(delnode.left)
        delnode.val = newdelnode.val
        self.delete_at(newdelnode)
        return delnode

    def find_max(self, root):
        if root.right is None:
            return root
        return self.find_max(root.right)
