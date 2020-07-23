class Queue():
    
    def __init__(self):
        self.items=[]
        
    def enqueue(self,item):
        self.items.insert(0,item)
        
    def dequeue(self):
        return self.items.pop()
        
    def is_empty(self):
        return self.items==[]
        
    def size(self):
        return len(self.items)
        
q=Queue()

q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)

print (q.dequeue())
print (q.dequeue())

print (q.is_empty())
print (q.size())

