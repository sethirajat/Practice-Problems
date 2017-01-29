'''
Program to find if there is a cycle in a directed graph
'''

class Node(object):

    def __init__(self,value):
        self.val = value
        self.outgoings = []


    def make_conn(self,node):
        self.outgoings.append(node)

    def give_neighbors(self):
        return self.outgoings



def isDAG(node):
    if node is None:
        return False

    
