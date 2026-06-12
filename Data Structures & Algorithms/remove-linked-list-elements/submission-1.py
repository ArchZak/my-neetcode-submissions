# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        #input: linked list of elms and target val to delete
        #output: same LL but all values deleted

        prev = dummy = ListNode(next=head)
        curr = dummy.next

        while curr:
            if curr.val == val:
                prev.next = curr.next
                curr = prev.next
            else:
                curr = curr.next
                prev = prev.next
            
        
        #0-1-1-None
        #0-1-None
        #

        return dummy.next