# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #return true is cycle in linked list is detected
        #youre given head which is beginning of the LL

        #need two pointers, one moving 2 at a time, another moving 1 at a time
        #if 2 encounters a null, LL isnt circular
        #if 1 == 2, then there's a loop

        slow, fast = head, head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

            if slow == fast:
                return True

        return False