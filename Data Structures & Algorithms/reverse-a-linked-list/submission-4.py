# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        temp = head

        while temp:
            after = temp.next # creates the next step
            temp.next = previous # points next backwards
            previous = temp 
            temp = after #move prev and current forward

        return previous