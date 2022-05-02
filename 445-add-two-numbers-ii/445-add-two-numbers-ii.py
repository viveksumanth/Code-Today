# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverseLinkedList(self,ll):
        if ll == None:
            return None
        nNodes = 0
        prev = None

        while(ll != None):
            nNodes += 1
            temp = ll.next
            ll.next = prev
            prev = ll
            ll = temp
        
        return prev,nNodes
    
    def addNodes(self,diff,head):
        
        ll = head
        while(ll.next != None):
            ll = ll.next
        
        while(diff):
            ll.next = ListNode(0)
            ll = ll.next
            diff -= 1
            
        return head
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        l1,nNodes1 = self.reverseLinkedList(l1)
        l2,nNodes2 = self.reverseLinkedList(l2)

        diff = nNodes1 - nNodes2
        if diff > 0: #add nodes to nNodes2
            l2 = self.addNodes(diff,l2)
        else:
            l1 = self.addNodes(abs(diff),l1)
        
        carry = 0
        
        temp = l1
         
        while(l1):
            l1.val = l1.val + l2.val + carry
            if l1.val >= 10:
                carry = l1.val//10
                l1.val = l1.val%10
            else:
                carry = 0
            
            l1 = l1.next
            l2 = l2.next
         
        
        result,nNodes = self.reverseLinkedList(temp)
        
        if carry:
            curr = ListNode(carry)
            curr.next = result
            result = curr
            
        return result
            
        