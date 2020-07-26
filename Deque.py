class Deque():
    def __init__(self):
        self.items=[]
        
    def addfront(self,item):
        self.items.append(item)
        
    def addrear(self,item):
        self.items.insert(0,item)
        
    def removefront(self):
        return self.items.pop()
        
    def removerear(self):
        return self.items.pop(0)
        
    def size(self):
        return len(self.items)
        
    def is_empty(self):
        return self.items==[]
        
d=Deque()

print(d.size())
print(d.is_empty())
d.addfront(5)
d.addrear(6)
print(d.size())
print(d.removefront())
print(d.removerear())
        

                        
                    
                    
        
            
            
    
            

    
    