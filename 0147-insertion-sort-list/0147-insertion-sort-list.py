# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sorted_head = None
        curr = head

        while curr:
            next_node = curr.next
            sorted_head = self.insert_node(sorted_head, curr)
            curr = next_node
        
        return sorted_head

    def insert_node(self, sorted_head, node):
        if not sorted_head or node.val < sorted_head.val:
            node.next = sorted_head
            sorted_head = node
        else:
            curr = sorted_head
            while curr.next and curr.next.val < node.val:
                curr = curr.next
            node.next = curr.next
            curr.next = node
        
        return sorted_head