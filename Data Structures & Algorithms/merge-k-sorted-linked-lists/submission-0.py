# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #input: a list of linked lists
        #output: a single linked list that's sorted

        #going to iterate through each linked list and then add the values to a minheap
        #building a heap from an unsorted list is O(n) and adding values is O(nlogn)
        #once we have the minheap, we'll pop values off and create a new linked list

        heap = []
        for head in lists:
            while head:
                heap.append(head.val)
                head = head.next

        heapq.heapify(heap)
        dummy = curr = ListNode()
        while heap:
            curr.next = ListNode(heapq.heappop(heap))
            curr = curr.next

        return dummy.next