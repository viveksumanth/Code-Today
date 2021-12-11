# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, llist: ListNode) -> ListNode:
        if llist == None:
            return 
        pointerA = llist
        temp = pointerB = llist


        while(pointerA):
            if pointerA.val != pointerB.val:
                pointerB = pointerB.next
                pointerB.val = pointerA.val

            pointerA = pointerA.next

        pointerB.next = None
        return temp