# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        #Input: head of two lists
        #return the node where the two lists intersect, or null

        #append nodes itself (so memory) in set
        #if the node is already in set, return that node
        #iterate through both lists

        tracker = set()

        while headA or headB:
            if headA is headB:
                return headA
            elif headA in tracker:
                return headA
            elif headB in tracker:
                return headB
            tracker.add(headA) if headA is not None else 0
            tracker.add(headB) if headB is not None else 0
            headA = headA.next if headA else None
            headB = headB.next if headB else None
            
        return None