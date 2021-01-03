# 1. implement Dequeue using linked list 
# 2. implement stack using Dll 
# 3. implement simple queue using DLL 
# 4. implement priority queue

# 1. implement Dequeue using linked list
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class Dequeue:
#     def __init__(self):
#         self.front=None
#         self.rear=None
#     def insert_front(self,data):
#         if(self.front==None):
#             self.front=self.rear=Node(data)
            
#         else:
#             new_node=Node(data)
#             new_node.next=self.front
#             self.front=new_node

#     def insert_rear(self,data):
#         if(self.rear==None):
#             self.rear=Node(data)
#         else:
#             new_node=Node(data)
#             self.rear.next=new_node
#             self.rear=new_node
#     def delete_front(self):
#         t=self.front
#         self.front=self.front.next
#         del t
#     def delete_rear(self):
#         t=self.front
#         while(t.next.next!=None):
#             t=t.next
#         self.rear=t
#         self.rear.next=None
        


#     def display(self):
#         print("the data is:")
#         t=self.front
#         while(t):
#             print(t.data)
#             t=t.next

# s=Dequeue()
# s.insert_front(2)
# s.insert_front(23)
# s.insert_front(24)
# s.insert_rear(32) 
# s.insert_rear(33)
# s.insert_rear(34) 
# s.display() 
# s.delete_rear()
# s.display() 
# s.delete_front()
# s.display()    

# # 2. implement stack using Dll
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.prev=None
#         self.next=None
# class Stack: 
#     # Function to initialize head  
#     def __init__(self): 
#         self.head=None
#         self.top=-1
          
# # Function to add an element data in the stack  
#     def push(self, data): 
  
#         if self.top==-1: 
#             self.head = Node(data) 
#             self.top+=1
#         else: 
#             n = Node(data)
#             self.head.prev=n
#             n.next=self.head
#             n.prev=None
#             self.head=n
#             self.top+=1
              
              
# # Function to pop top element and return the element from the stack  
#     def pop(self): 
  
#         if self.top==-1: 
#             print("list is empty") 
#         elif self.head.next is None: 
#             temp = self.head.data 
#             self.head = None
#             return temp 
#             self.top-=1
#         else: 
#             temp = self.head.data 
#             self.head = self.head.next
#             self.head.prev = None
#             return temp  
#             self.top-=1
# # Function to return top element in the stack  
#     def top(self): 
  
#         return self.head.data 
# # Function to return the size of the stack  
#     def size(self): 
  
#         temp = self.head 
#         count = 0
#         while temp is not None: 
#             count = count + 1
#             temp = temp.next
#         print( "the size is",count)      
# # Function to check if the stack is empty or not   
#     def isEmpty(self): 
  
#         if self.top==-1: 
#            return True
#         else: 
#            return False
# # Function to print the stack 
#     def printstack(self): 
          
#         print("stack elements are:") 
#         temp = self.head 
#         while temp is not None: 
#             print(temp.data) 
#             temp = temp.next
# s=Stack()
# s.push(5)
# s.push(4)
# s.push(3)
# s.printstack()
# s.size() 
# s.pop()
# s.size()
# s.printstack()

# 3. implement simple queue using DLL 
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
#         self.prev=None
# class queue:
#     def __init__(self):
#         self.front=None
#         self.rear=None
#     def insert_rear(self,data):
#         if (self.rear==None):
#             self.front=self.rear=Node(data)
#         else:
#             new_node=Node(data)
#             new_node.next=self.rear
#             self.rear.prev=new_node
#             self.rear=new_node
#     def delete_front(self):
#         self.front=self.front.prev
#         self.front.next=None
#     def display(self):
#         t=self.front
#         while(t):
#             print(t.data)
#             t=t.prev
# s=queue()
# s.insert_rear(9)
# s.insert_rear(10)
# s.insert_rear(11)
# s.insert_rear(12)
# s.insert_rear(13)
# s.display()
# s.delete_front()
# s.delete_front()
# s.display()

#4. implement priority queue
# class PriorityQueue(object): 
#     def __init__(self): 
#         self.queue = []   
#     def isEmpty(self): 
#         return len(self.queue) == 0
#     def insert(self, data): 
#         self.queue.append(data) 
#     def delete(self): 
#             max = 0
#             for i in range(len(self.queue)): 
#                 if self.queue[i] > self.queue[max]: 
#                     max = i 
#             item = self.queue[max] 
#             del self.queue[max] 
#             return item     
# p = PriorityQueue() 
# p.insert(12) 
# p.insert(1) 
# p.insert(14) 
# p.insert(7) 
# p.insert(23)
# p.insert(3)
# print(p)             
# while not p.isEmpty(): 
#     print(p.delete())

# #implementation of queues using arrays  
# class Queue: 
#     def __init__(self): 
#         self.s1 = [] 
#         self.s2 = [] 
  
#     # EnQueue item to the queue 
#     def enQueue(self, x): 
#         self.s1.append(x) 
  
#     # DeQueue item from the queue 
#     def deQueue(self): 
  
#         # if both the stacks are empty 
#         if len(self.s1) == 0 and len(self.s2) == 0: 
#             print("Q is Empty") 
#             return
  
#         # if s2 is empty and s1 has elements 
#         elif len(self.s2) == 0 and len(self.s1) > 0: 
#             while len(self.s1): 
#                 temp = self.s1.pop() 
#                 self.s2.append(temp) 
#             return self.s2.pop() 
  
#         else: 
#             return self.s2.pop() 
  
#     # Driver code 
 
# q = Queue() 
# q.enQueue(1) 
# q.enQueue(2) 
# q.enQueue(3) 

# print(q.deQueue()) 
# print(q.deQueue()) 
# print(q.deQueue()) 