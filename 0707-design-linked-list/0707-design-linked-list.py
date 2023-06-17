class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        
    

class MyLinkedList:
    
    def __init__(self):
        self.head = Node(0)
        self.tail = self.head
        
       

    def get(self, index: int) -> int:
        curr = self.head.next
        counter = 0
        while(curr):
            
            if counter == index:
                return curr.val
            # print(curr.val)
            curr = curr.next
            counter += 1
            
        return -1
                
        
        

    def addAtHead(self, val: int) -> None:
        
        
        new_node = Node(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if self.head == self.tail:
            self.tail = self.tail.next
        
        
        
        
        

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        curr = self.head.next
        if curr == None:
            new_node.next = self.head.next
            self.head.next = new_node
            
        else:    
            while(curr):
                prev = curr
                curr = curr.next
            prev.next = new_node
            prev = new_node
        # print(prev.val)
        new_node.next = None
        # self.tail.next = new_node
        # self.tail = self.tail.next
        
        # curr = head
        # while(curr and curr.next):
        #     curr = curr.next
        # curr.next = new_node
       
        
        
        

    def addAtIndex(self, index: int, val: int) -> None:
        count = 0
        curr = self.head.next
        new_node = Node(val)
        
        prev1 = curr
        if curr == None and index == 0:
            new_node.next = self.head.next
            self.head.next = new_node
            
            
            
        
        while(curr):
            if index == 0:
                new_node.next = self.head.next
                self.head.next = new_node
               
            elif index == count:
                new_node.next = curr
                prev1.next = new_node
               
            prev1 = curr 
            # print(prev1.val)
            curr = curr.next
            count += 1
        
        if count == index and count != 0 :
            prev1.next = new_node
            prev1 = new_node
            prev1.next = None
        
    
    def deleteAtIndex(self, index: int) -> None:
        count = 0
        curr = self.head.next
        prev = self.head
        
        while(curr):
            
            if index == 0:
                temp = curr.next
                # prev.next = temp
                # prev = temp
                curr.next = None
                curr = temp
                
               
            elif index == count:
                temp  = curr.next
                # prev.next = temp
                curr.next = None
                curr = temp
            prev.next = curr
            prev = curr
            if (curr):
                print(curr.val) 
            # prev = curr
            
            if curr:
                curr = curr.next
            count += 1
            # print(prev.val)
                
            
                
                
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)