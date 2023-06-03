# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return 
        curr = head
        temp = curr.next
        
        while(temp):
            if curr.val == temp.val:
                curr.next = temp.next
                
            else:
                curr = curr.next
            temp = temp.next
        return head
        