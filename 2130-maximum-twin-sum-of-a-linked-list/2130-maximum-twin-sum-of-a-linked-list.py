# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head
        
        while(fast and fast.next):
            fast = fast.next.next
            slow = slow.next
        
        prev = None
        while(slow):
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        maxim = 1
        while(prev):
            maxim = max(maxim , prev.val + head.val)
            prev = prev.next
            head = head.next
        return maxim
            
            
        
        
      