# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode],result = ListNode(0)) -> Optional[ListNode]:
        
        if head == None:
            return head
        
        dummy = pointerA = head
        pointerB = head.next
        
        while(pointerB):
            
            temp = pointerA.val
            pointerA.val = pointerB.val
            pointerB.val = temp
            
            if pointerB.next and pointerB.next.next:
                pointerA = pointerA.next.next
                pointerB = pointerA.next
                
            else:
                break
        
        return dummy   
            
            
            
            
            