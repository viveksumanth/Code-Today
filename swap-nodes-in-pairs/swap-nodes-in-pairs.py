# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        '''        
                 "1 -> 2"  -> "3 -> 4" -> 5

                  |    |       |    |    |

                 "2 -> 1"  -> "4 -> 3" -> 5

        '''
        temp = ListNode(0)
        temp.next = head
        
        while(head and head.next):
            
            temp1 = head.val
            temp2 = head.next.val
            head.val = temp2
            head.next.val = temp1
            head = head.next.next
        
        # print(temp.next)
        return temp.next
            
            
            
            