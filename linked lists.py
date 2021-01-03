# #insertion at end
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
  
# def print_list(t):
#     while(t):
#         print(t.data)
#         t=t.next
# def insert_end(t):
#     n=Node(24)
#     while(t.next!=None):
#         t=t.next
#     t.next=n
#     n.next=None
    
# head=None
# for i in range(3):
#     if head==None:
#         head=n=Node(i)
#     else:
#         n.next=Node(i)
#         n=n.next   
# print_list(head)
# insert_end(head)
# print_list(head)

 
# #insertion at begining
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
  
# def print_list(t):
#     while(t):
#         print(t.data)
#         t=t.next
# def insert_end(t):
#     n=Node(24)
#     while(t.next!=None):
#         t=t.next
#     t.next=n
#     n.next=None
# def insert_start(t):
#     n=Node(240)
#     n.next=t
#     global head
#     head=n     
# head=None
# for i in range(3):
#     if head==None:
#         head=n=Node(i)
#     else:
#         n.next=Node(i)
#         n=n.next   
# print_list(head)
# insert_end(head)
# print_list(head)
# insert_start(head)
# print_list(head)

##insertion at particular position
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
  
# def print_list(t):
#     while(t):
#         print(t.data)
#         t=t.next
# def insert_end(t):
#     n=Node(24)
#     while(t.next!=None):
#         t=t.next
#     t.next=n
#     n.next=None
# def insert_start(t):
#     n=Node(240)
#     n.next=t
#     global head
#     head=n 
    
# def insert_at_position(t):
#     pos=int(input("enter the number"))   
#     n=Node(30)
#     c=1
#     while(c < pos):
#         t = t.next
#         c += 1
#     n.next=t.next
#     t.next=n
# head=None
# for i in range(3):
#     if head==None:
#         head=n=Node(i)
#     else:
#         n.next=Node(i)
#         n=n.next   
# print_list(head)
# insert_end(head)
# print_list(head)
# insert_start(head)
# print_list(head)
# insert_at_position(head)
# print_list(head)

# #deletion at end
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
  
# def print_list(t):
#     while(t):
#         print(t.data)
#         t=t.next
# def del_end(t):
#     n=Node(24)
#     while(t.next!=None):
#         n=t
#         t=t.next
#     print('the deleted node or value',t.data) 
#     n.next=None      
# head=None
# for i in range(6):
#     if head==None:
#         head=n=Node(i)
#     else:
#         n.next=Node(i)
#         n=n.next   
# print_list(head)
# del_end(head)
# print_list(head)

# #deletion at start
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
  
# def print_list(t):
#     while(t):
#         print(t.data)
#         t=t.next
# def del_end(t):
#     n=Node(24)
#     while(t.next!=None):
#         n=t
#         t=t.next
#     print('the deleted node or value',t.data) 
#     del t
#     n.next=None  
# def del_start(t): 
#     n=t 
#     global head 
#     head=head.next
#     print('the deleted node or value',t.data)
#     del t      
# head=None
# for i in range(6):
#     if head==None:
#         head=n=Node(i)
#     else:
#         n.next=Node(i)
#         n=n.next   
# print_list(head)
# del_end(head)
# print_list(head)
# del_start(head)
# print_list(head)

# #deletion at position
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
  
# def print_list(t):
#     while(t):
#         print(t.data)
#         t=t.next
# def del_end(t):
#     n=Node(24)
#     while(t.next!=None):
#         n=t
#         t=t.next
#     print('the deleted node or value',t.data) 
#     del t
#     n.next=None  
# def del_start(t): 
#     n=t 
#     global head 
#     head=head.next
#     print('the deleted node or value',t.data)
#     del t 
# def del_inpos(t):
#     pos=int(input("enter the nuumber"))
#     c=1
#     while(c<=pos):
#         n=t
#         t=t.next
#         c+=1
#     n.next=t.next    
#     print('the deleted node or value',t.data)
#     del t
# head=None
# for i in range(6):
#     if head==None:
#         head=n=Node(i)
#     else:
#         n.next=Node(i)
#         n=n.next   
# print_list(head)
# del_end(head)
# print_list(head)
# del_start(head)
# print_list(head)
# del_inpos(head)
# print_list(head)

## printing Dll both backward and forward
# class Node:
#     def __init__(self,data):
#         self.prev=None
#         self.data=data
#         self.next=None
  
# def print_forwlist(t):
#     while(t):
#         print(t.data)
#         t=t.next
# def print_backlist(t):
#     while(t):
#         print(t.data)
#         t=t.prev        
# head=None
# for i in range(6):
#     if head==None:
#         head=n=Node(i)
#     else:
#         t=n
#         n.next=Node(i)
#         n=n.next
#         n.prev=t 
# tail=n                
# print_forwlist(head)
# print_backlist(tail)

# #insertion at start,end ,position in 
# class Node:
#     def __init__(self,data):
#         self.prev=None
#         self.data=data
#         self.next=None
  
# def print_forwlist(t):
#     print("dll")
#     while(t):
#         print(t.data)
#         t=t.next
# def print_backlist(t):
#     print("dll")
#     while(t):
#         print(t.data)
#         t=t.prev 
# def insert_start(t):
#     n=Node(22)
#     n.next=t
#     t.prev=n
#     global head
#     head=n
#     n.prev=None
# def insert_end(t):
#     n=Node(33)
#     n.prev=t
#     t.next=n
#     tail=n
#     tail.next=None 
# def insert_atpos(t):
#     n=Node(44)
#     pos=int(input("enter the nuumber"))
#     c=0
#     while(c < pos):
#         t = t.next
#         c += 1
#     n.prev=t    
#     n.next=t.next
#     t.next=n
#     t=n.next 
#     t.prev=n  

# head=None
# for i in range(6):
#     if head==None:
#         head=n=Node(i)
#     else:
#         t=n
#         n.next=Node(i)
#         n=n.next
#         n.prev=t 
# tail=n                
# print_forwlist(head)
# print_backlist(tail)
# insert_start(head)
# print_forwlist(head)
# insert_end(tail)
# print_forwlist(head)
# insert_atpos(head)
# print_forwlist(head)

#deletion at start,end,at position
# class Node:
#     def __init__(self,data):
#         self.prev=None
#         self.data=data
#         self.next=None
  
# def print_forwlist(t):
#     print("dll")
#     while(t):
#         print(t.data)
#         t=t.next
# def delete_at_start(t):
#     global head
#     head=t.next
#     t.next.prev=None
# def delete_at_end(t):
#     global tail
#     tail.prev.next=None
# def delete_at_position(t):
#     p=int(input())
#     c=1
#     while(c<p):
#         c+=1
#         t=t.next
#     t.next=t.next.next
#     t.next.prev=t
# head=None
# for i in range(6):
#     if head==None:
#         head=n=Node(i)
#     else:
#         t=n
#         n.next=Node(i)
#         n=n.next
#         n.prev=t 
# tail=n        
# print_forwlist(head)
# print('after deleting at start')
# delete_at_start(head)
# print_forwlist(head)
# print('after deleting at end')
# delete_at_end(head)
# print_forwlist(head)
# print('after deleting at a certain postion')
# delete_at_position(head)
# print_forwlist(head)  

# # program for delete an element in a dll

# class Node:
#     def __init__(self,data):
#         self.prev=None
#         self.data=data
#         self.next=None
        
# # function for printing the elements in the DLL
# def print_dll(t):
#     print('The values in the Dll are : ')
#     while(t!=None):
#         print(t.data)
#         t=t.next
# def del_head(t):
#     global head
#     t=head
#     print('The deleted element is',head.data)
#     head=head.next
#     head.prev=None
#     del t

# # deleting the last node in the list
# def del_tail(t):
#     global tail
#     t=tail
#     print('The deleted element is',tail.data)
#     tail=tail.prev
#     tail.next=None
#     del t

# # deleting the node inbetween any two existing nodes
# def del_pos(t):
#     # move until we reach the pos-1 node
#     counter=1
#     pos=int(input('enter the position of the node to be deleted'))
#     while(counter<pos):
#         counter+=1
#         n=t
#         t=t.next
#     n.next=t.next
#     t.next.prev=n
#     print('The deleted element is',head.data)
#     del t
# head=None
# choice='y'
# while(choice=='y'):
#     val=int(input('Enter a number'))
#     if head==None:
#         n=head=Node(val)
#     else:
#         t=n
#         n.next=Node(val)
#         n=n.next
#         n.prev=t
#     choice=input('want to create another node y/n')
# tail=n    
# print_dll(head)

# print('The actual list')
# print_dll(head)
# del_head(head)
# # del_pos(head)
# # print('The modified list after deletion is')
# print_dll(head)
# del_tail(head)
# print_dll(head)

# # program for creating a circularly single linked list
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# # code for creating a Circular SLL
# head=None
# for i in range(5):
#     if head==None:
#         n=head=Node(i)
#     else:
#         n.next=Node(i)
#         n=n.next
# # hold the address of header node in the next portion of tail node
# n.next=head

# # print the elements in the csll
# print('The lement in the Circularly linked list are:')
# n=head
# print(n.data)
# n=n.next
# while(n!=head):
#     print(n.data)
#     n=n.next

