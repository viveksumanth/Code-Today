# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:
    def mergeKLists(self, lists):
        heapArray = []
        
        self.dummyHead = self.head = ListNode('X')
        
        if len(lists) == 0:
            return None
        
        for eachHead in lists:
            if eachHead:
                heapq.heappush(heapArray,[eachHead.val,eachHead])
            
        while(heapArray):
            
            nextSmallest,listHead = heapq.heappop(heapArray)
            if listHead.next:
                heapq.heappush(heapArray,[listHead.next.val,listHead.next])
            self.head.next = ListNode(nextSmallest)
            self.head = self.head.next
        

        return self.dummyHead.next
            
        