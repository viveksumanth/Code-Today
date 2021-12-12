# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        
        |
        1 -> 2 -> 3 -> 4 -> 5
        
        
        5 -> 4 -> 3 -> 2 -> 1
        
        
        '''
        '''
        
        if head == None:
            return None
        
        prev = None
        current = head

        while(current):
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        
        return prev
        
        '''
        
        if head == None or head.next == None:
            return head
        
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p
    
    