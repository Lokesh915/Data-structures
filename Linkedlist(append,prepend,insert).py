class Node:
    
    def __init__(self,data):
        self.data=data
        self.next=None
        
class Linkedlist:
    def __init__(self):
        self.head=None
        
    def print_list(self):
        tracker=self.head
        while  tracker:
            print(tracker.data)
            tracker=tracker.next
        
    def append(self,data):
        new_node=Node(data)
        
        if self.head==None:
            self.head=new_node
            
        else:
            current=self.head
            while current.next:
                current=current.next
            
            current.next=new_node
    def prepend(self,data):
        new_node=Node(data)
        
        if self.head==None:
            self.head=new_node
            
        else:
            new_node.next=self.head
            self.head=new_node
            
    def insert(self,key,data):
        new_node=Node(data)
        if self.head==None:
            new_node=self.head
            
        elif key is None:
            print("invalid key")
        else:
            new_node.next=key.next
            key.next=new_node
            
    
llist=Linkedlist()
llist.append(2)
llist.append(3)
llist.append(4)
llist.append(5)
llist.prepend(6)
llist.insert(llist.head.next.next,7)


llist.print_list()

        
