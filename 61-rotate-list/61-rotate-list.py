# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
#     def __init__(self):
#         self.length = 0
    
#     def lengthOfList(self,head):
        
#         while(head):
#             self.length += 1
#             head = head.next
            
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # find the length of the list
        tempHead = head
        length = 1
        
        if k == 0:
            return head
        
        if head == None:
            return head
        
        while(tempHead.next != None):
            length += 1
            tempHead = tempHead.next
        
        tempHead.next = head
        
        k= length - (k%length)
            
        while(k-1):
            head = head.next
            k -= 1

        newHead = head.next
        head.next = None
        
        return newHead