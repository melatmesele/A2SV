class MyQueue:

    
    def __init__(self):
        self.enqueue_stack = []
        self.dequeue_stack = []
    
   
    def push(self, x: int) -> None:
        self.enqueue_stack.append(x)
        
    
    def pop(self) -> int:
        
        if not self.dequeue_stack:
            self.fill()
            
       
        return self.dequeue_stack.pop()

    def peek(self) -> int:
        if not self.dequeue_stack:
            self.fill()

        
        temp = self.dequeue_stack.pop()
        self.dequeue_stack.append(temp)
        return temp
    
    def empty(self) -> bool:
        return not len(self.dequeue_stack) and not len(self.enqueue_stack)
    def __init__(self):
        self.enqueue_stack = []
        self.dequeue_stack = []
    
    def push(self, x: int) -> None:
        self.enqueue_stack.append(x)
        
  
    def pop(self) -> int:
       
        if not self.dequeue_stack:
            self.fill()
            
        
        return self.dequeue_stack.pop()

    def peek(self) -> int:
        if not self.dequeue_stack:
            self.fill()

       
        temp = self.dequeue_stack.pop()
        self.dequeue_stack.append(temp)
        return temp
    
    def empty(self) -> bool:
        return not len(self.dequeue_stack) and not len(self.enqueue_stack)
    
  
    
    def fill(self):
        while self.enqueue_stack:
            self.dequeue_stack.append(self.enqueue_stack.pop())
    
   
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()