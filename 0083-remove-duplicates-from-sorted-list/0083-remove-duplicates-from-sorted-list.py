# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return 
        dummyNode = ListNode(-1000 ,None)
        prev = dummyNode
        curr = head
        while(curr):
            if prev.val != curr.val:
                prev.next = curr
                prev = curr
            curr = curr.next
        prev.next = None
        return dummyNode.next
                
#         curr = head
#         temp = curr.next
        
#         while(temp):
#             if curr.val == temp.val:
#                 curr.next = temp.next
                
#             else:
#                 curr = curr.next
#             temp = temp.next
#         return head
        