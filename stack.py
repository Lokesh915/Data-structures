class Stack():
   
    def __init__(self):
        self.items = []
    
    def push(self, i):
        self.items.append(i)
    
    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        return self.items == []
        
    def peek(self):
        return self.items[-1]
        
    def get_stack(self):
        return self.items
        
s=Stack()

s.push('a')
s.push('b')

print(s.get_stack())
print(s.pop())
print(s.is_empty())
s.push('b')
print(s.peek())