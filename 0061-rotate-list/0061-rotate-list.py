# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count ,curr = 0 , head
        if (head == None):
            return
        
        while(curr):
            count += 1
            curr = curr.next
        if count == 1 or k == 0:
            return head
        
        length  = count 
        if k > length:
            result = length - (k%length)
            if result == length:
                return head
        else :
            result = length - k 
        
        # while(result < 0):
        #     result += count
        if result == 0:
            return head
        
        counter , great = 0 ,None 
        dummyNode = ListNode(0 , None)
        prev = dummyNode
        lastNode = None
        
        
        current = head
        while(current):
            
            if counter == result:
                lastNode = prev
                great = current
            else:
                prev.next = current
                prev = current
                current  = current.next
            counter +=1
        prev.next = dummyNode.next
        dummyNode.next = great
        lastNode.next = current
        return dummyNode.next
        
        
        
        