# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #input: two nonempty LL with non negative integers
        #ints are reverse order in LL, each node is single digit, otw make it 0
        #output: return the sum of the two nums as LL

        dummy = curr = ListNode(0)
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            val_sum = val1+val2+carry

            mod = val_sum%10
            carry = val_sum//10

            curr.next = ListNode(mod)
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
