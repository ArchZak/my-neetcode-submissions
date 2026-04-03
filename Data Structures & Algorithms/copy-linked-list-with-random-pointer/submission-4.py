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
        # input: given a LL with val, next, and random
        # output: deep copy of the list

        # multiple passes
        # first pass to construct val and next of new LL
        # ^ store each node of given LL with corresponding node of our LL
        # second pass to put in random nodes
        
        hash_dict = {}
        dummy = curr1 = Node(0)
        curr2 = head

        while curr2:
            curr1.next = Node(curr2.val) #next and random defaults to none

            hash_dict[curr2] = curr1.next #corresponding dict

            curr1 = curr1.next
            curr2 = curr2.next

        curr2 = head
        curr1 = dummy.next

        while curr2:
            if curr2.random: #so if its not null
                curr1.random = hash_dict[curr2.random] #will get OUR node now
            else:
                curr1.random = None #dict doesnt like to index none

            curr1 = curr1.next
            curr2 = curr2.next


        return dummy.next

    