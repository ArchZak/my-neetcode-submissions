"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #input: head of singly LL, where nodes have val, next, random
        #output: output a deep copy of the list

        #first pass: create the val and next
        #also make a dict that stores randoms. key = head node, value = corresponding our node

        #second pass: inits randoms
        #if head.random, then make our curr node point to corresponding random

        dummy = curr1 = Node(x=0)
        curr2 = head
        hash_dict={}

        while curr2:
            curr1.next = Node(x=curr2.val)
            hash_dict[curr2] = curr1.next #key = head node, value = our node

            curr1 = curr1.next
            curr2 = curr2.next

        curr1 = dummy.next
        curr2 = head

        while curr2:
            if curr2.random:
                curr1.random = hash_dict[curr2.random]
            else:
                curr1.random = None

            curr1 = curr1.next
            curr2 = curr2.next

        return dummy.next
