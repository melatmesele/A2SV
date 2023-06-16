# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = None
        curr1 ,curr2 = l1 , l2 
        prev1 ,prev2 = None , None
        dummyNode = ListNode(0 , None)
        prev = dummyNode
        remain = 0
        while(curr1 or curr2):
            if curr1 and curr2 == None:
                result = remain + curr1.val
                remain = result // 10 
                value = result % 10
                values = ListNode(value ,None)
                prev.next = values
                prev = values
                curr1 = curr1.next
            elif curr2 and curr1 == None:
                
                result = remain + curr2.val
                
                remain = result // 10 
                value = result % 10
                values = ListNode(value ,None)
                prev.next = values
                prev = values
                curr2 = curr2.next
            elif curr2 and curr1:
                result = remain + curr1.val  + curr2.val
                value = result % 10
                remain = result // 10 
                values = ListNode(value ,None)
                prev.next = values
                prev = values
                curr1 ,curr2 = curr1.next ,curr2.next
        if remain == 1:
            prev.next = ListNode(1 , None)
        return dummyNode.next
            
            
            
            
       