class MyQueue:

    def __init__(self):
        self.stack = list()

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        temp = list()
        while self.stack:
            val = self.stack.pop()
            temp.append(val)

        res = temp.pop()
        while temp: 
            self.stack.append(temp.pop()) 
        
        return res

    def peek(self) -> int:
        temp = list()
        while self.stack: 
            val = self.stack.pop() 
            temp.append(val)

        res = temp.pop()
        self.stack.append(res) 
        while temp: 
            self.stack.append(temp.pop()) 
        

        return res

    def empty(self) -> bool:
        return not self.stack
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()