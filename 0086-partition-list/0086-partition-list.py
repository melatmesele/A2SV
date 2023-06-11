# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummyGreat = ListNode(0, None)
        dummySmall = ListNode(0, None)
        
        prevGreat = dummyGreat
        prevSmall = dummySmall
        curr = head
        while(curr):
            if curr.val < x:
                prevSmall.next = curr
                prevSmall = curr
                curr = curr.next
            else:
                prevGreat.next = curr
                prevGreat = curr
                curr = curr.next
        prevSmall.next = dummyGreat.next
        prevGreat.next = None
        
        return dummySmall.next
        
            
                
               
                
                