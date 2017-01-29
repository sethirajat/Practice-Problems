'''
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.
'''
# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head is None:
            return None

        assigned = {}
        curr = head
        prev = newhead = RandomListNode(curr.label)
        assigned[curr] = prev
        while curr.next is not None:
            curr = curr.next
            newnode = RandomListNode(curr.label)
            assigned[curr] = newnode
            prev.next = newnode
            prev = prev.next

        curr = head
        newcurr = newhead
        while curr is not None:
            newcurr.random = assigned[curr.random]
            curr = curr.next
            newcurr = newcurr.next

        return newhead