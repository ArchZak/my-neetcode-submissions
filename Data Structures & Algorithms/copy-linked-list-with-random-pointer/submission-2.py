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
        dummy = curr1 = Node(x=0) 
        curr2 = head

        hash_list = {}

        while curr2:
            curr1.next = Node(x=curr2.val)
            hash_list[curr2] = curr1.next

            curr1 = curr1.next
            curr2 = curr2.next

        hash_list[None] = curr1.next
        
        curr1 = dummy.next
        curr2 = head

        while curr2:
            curr1.random = hash_list[curr2.random]
            
            curr1 = curr1.next
            curr2 = curr2.next

        print(hash_list)

        return dummy.next