# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow , fast = head , head
        
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if head and head.next and head.next.next and slow != fast:
            return None
        elif not head or not head.next or not head.next.next:
            return None             
        else:
            fast = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return fast
                
        