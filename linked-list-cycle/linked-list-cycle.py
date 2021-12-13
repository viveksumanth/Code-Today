# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False

        fast = slow = head
        isCycle = False
        while(fast != None and fast.next != None):
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                isCycle = True
                break

        return isCycle
        