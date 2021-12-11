# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        
        dummyNode = ListNode(-1000)
        dummyNode.next = head
        
        result = pointerB = dummyNode
        pointerA = head
        
        while(pointerA != None):
            
            if pointerA.next and pointerA.next.val == pointerB.next.val:
                
                while(pointerA.next and pointerA.next.val == pointerB.next.val):
                    pointerA = pointerA.next
                
                pointerB.next = pointerA.next
                    
            else:
                pointerB = pointerB.next
            
            pointerA = pointerA.next
        
        return result.next