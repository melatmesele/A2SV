# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        evenDummy = ListNode(0,None)
        even  = evenDummy
        oddDummy = ListNode(0,None)
        odd = oddDummy
        if head == None:
            return
        curr = head
        counter = 1
        while(curr):
            if counter % 2 != 0:
                odd.next = curr
                odd = curr
                curr = curr.next
            else:
                even.next = curr
                even = curr
                curr = curr.next
            counter += 1
        odd.next = evenDummy.next
        even.next = None
        return oddDummy.next
                
                
                
            
        
#         if head == None:
#             return 
#         odd = head
#         even = odd.next
#         even_head = even
        
#         while even != None and even.next:
#             odd.next = even.next
#             odd = odd.next
            
#             even.next = odd.next
#             even = even.next
#         odd.next = even_head
#         return head
        