# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        curr = head
        nodes = []
        
        while(curr):
            nodes.append(curr.val)
            curr = curr.next
        result = [0]* len(nodes)
        stack = []
        
        for index , value in enumerate(nodes):
            
            while(stack and nodes[stack[-1]] < value):
                result[stack.pop()]  = value
            
            stack.append(index)
        return result
            
        