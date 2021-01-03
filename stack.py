#stack program
# class Stack:   
#     def __init__(self):        
#         self.stack =[]         
#         self.top=-1     # function for inserting or pushing an element into stack     
#     def push(self,elt):         
#         self.top+=1 
#         self.stack.append(elt)            # function is to find whether the stack is empty or not     
#     def is_empty(self):         
#         if (len(self.stack))==0:             
#             return True           # function for deleting or poping an element from stack
#     def Pop(self):
#         if (self.is_empty()):             
#             print('Stack underflow')        
#         else:             
#             print('The deleted element from the stack is', self.stack.pop())       
#             self.top-=1                   # function for printing the elements in the stack     
#     def display(self):         
#         if (self.is_empty()):
#             print('Stack is empty')         
#         else:             
#             print('The elements in the stack ')             
#             for i in range(self.top,-1, -1):                 
#                 print(self.stack[i])
#             print(self.stack)    

# #driver code 
# s=Stack() 
# s.push(555) 
# s.push(20) 
# s.push(339) 
# s.push(44) 
# # delete elt. from stack
# s.Pop()
# s.Pop()
# s.display()
# #s.Pop()
# #s.Pop()
# s.display()
# s.Pop()

#model 2
# class Stack:
#     def __init__(self,capacity):
#         self.capacity = capacity
#         self.stack = []*capacity

#     def is_empty(self):
#         return len(self.stack)==0

#     def is_full(self):
#         return len(self.stack)==self.capacity

#     def push(self,val):
#         if self.is_full():
#             print('Stack is full!!! ')
#         else:
#             self.stack.append(val)
#         return self.stack

#     def pop(self):
#         if self.is_empty():
#             print('Stack is empty!!!')
#         else:
#            temp = self.stack.pop(len(self.stack)-1)
#            print('pop = ',temp)

#     def peek(self):
#         print(self.stack[-1])
           
#     def print_stack(self):
#         print(self.stack)

# s = Stack(5)
# s.print_stack()
# s.pop()
# s.push(10)
# s.push(10)
# s.push(10)
# s.push(20)
# s.push(20)
# s.push(20)
# s.pop()
# s.pop()
# s.print_stack()
# s.peek()

# program for implementing  a stack using a linked list
# class Node:
#     def __init__(self,data):
#         self.data=data
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
#             n.next=self.head           
#             self.head=n
#             self.top+=1
              
              
# # Function to pop top element and return the element from the stack  
#     def pop(self): 
  
#         if self.top==-1: 
#             print("list is empty") 
#         elif self.head.next is None: 
#             temp = self.head.data 
#             self.head = None
#             print(temp) 
#             self.top-=1
#         else: 
#             temp = self.head.data 
#             self.head = self.head.next
#             print(temp)  
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