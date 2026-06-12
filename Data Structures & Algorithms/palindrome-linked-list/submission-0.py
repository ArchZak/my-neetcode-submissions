# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #input: linked list
        #output: if ll is palindrome or not

        #loop through list and create string
        #then return comp of the string

        answer = ""

        while head:
            answer+=f"{head.val}"
            head = head.next

        return answer == answer[::-1]