#Write code in Python to implement the following:

#Implement A SLL by accepting the data to be stored into the linked list from user
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# def print_list(t):
#     while(t):
#         print(t.data)
#         t=t.next
# head=None
# print('enter the elements of a list')
# for i in range(0,5):
#     l=int(input())
#     if head==None:
#         head=n=Node(l)
#     else:
#         n.next=Node(l)
#         n=n.next
# print('printing the user entered elements')
# print_list(head)

# 2.  Linear search on SLL
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None       
# def linear_search(t,p):
#     t=head
#     while t is not None:
#         if t.data==p:
#             print(Node(p))
#             break
#         t=t.next
#     else :
#         print("element not found")             
# head=None        
# for i in range(6):
#     if head==None:
#         head=n=Node(i)
#     else:
#         n.next=Node(i)
#         n=n.next 
# linear_search(head,4)   

# 3. Insert a new node basing on the key value. if key is found insert the new node after the key value.  if key value is not found add the new node at the end of the existing list
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# def insert_value(t,p,i):
#     n=Node(i)
#     while(t):
#         if(t.data==p):
#             n.next=t.next
#             t.next=n            
#         t=t.next          
# def print_list(t):
#     while(t):
#         print(t.data)
#         t=t.next
# head=None
# print('enter the elements of a list')
# for i in range(0,5):
#     l=int(input())
#     if head==None:
#         head=n=Node(l)
#     else:
#         n.next=Node(l)
#         n=n.next
# insert_value(head,3,30)
# print('elements after insertion')
# print_list(head)

# 4. Reverse the elements of the linked list

#       a. By swapping the values in the list without changing the links
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
# def print_list(t):
#     while(t):
#         print(t.data)
#         t=t.next
# def reverse(t,k):
#     global m
#     for i in range(1,(m//2)+1):
#         if i==1:
#             t.data,k.data=k.data,t.data
#             t=t.next
#         else:

#             c=i
#             l=t
#             while c<=m-i-1:
#                 l=l.next
#                 c+=1
#             t.data,l.data=l.data,t.data 
#             t=t.next         
# head=None 
# m=int(input())       
# for i in range(1,m):
#     if head==None:
#         head=n=Node(i)
#     else:
#         n.next=Node(i)
#         n=n.next 
# tail=n
# print_list(head) 
# reverse(head,tail)
# print_list(head)     

#       b. By swapping the position of the nodes
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None       
# def print_list(t):
#     print("the sll")
#     while(t!=None):
#         print(t.data)
#         t=t.next  
# def reverse(t):
#     c=t
#     Next=None
#     Prev=None
#     while c:
#         Next = c.next
#         c.next = Prev
#         Prev=c
#         c=Next
#     head=Prev 
# head=None    
# for i in range(0,5):
#     if head==None:
#         head=n=Node(i)
#     else:
#         n.next=Node(i)
#         n=n.next
# tail=n
# print_list(head)
# reverse(head)
# print_list(tail) 

# 5. count the number of nodes in the list
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
       
# def print_list(t):
#     while(t):
#         print(t.data)
#         t=t.next
# def count(t) :
#     c=0
#     while(t!=None):
#         t=t.next
#         c+=1
#     print("the count is",c)           
# head=None
# for i in range(0,5):
#     if head==None:
#         head=n=Node(i)
#     else:
#         n.next=Node(i)
#         n=n.next
# tail=n
# print_list(head)
# count(head)


#6. Create a SLL to store particulars of  students such as (rollno, name and branch) in each node. store atleast 4 students particulars
# class Node:
#     def __init__(self, name,rollno,branch):
#         self.name = name
#         self.rollno=rollno
#         self.branch=branch
#         self.next = None
# def print_list(t):
#     while(t):
#         print(t.name,t.rollno,t.branch)
#         t=t.next         
# head=None
# for i in range(0,5):
#     x=int(input("roll"))
#     y=str(input("name"))
#     z=str(input("Branch"))
#     if head==None:
#         head=n=Node(x,y,z)
#     else:
#         n.next=Node(x,y,z)
#         n=n.next
# print_list(head)        

#7. create a SLL list in reverse order i.e store None in the first node and let the second node have the address of the first node.  store the address of the last node in header node.
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
# def print_list(t):
#     while(t):
#         print(t.data)
#         t=t.next
# def reverse(t):
#     print("sll")
#     for i in range(1,4):
#         global head
#         t=head
#         c=0
#         while c+i<3:
#             t=t.next
#             c+=1
#         print(t.data)    

# head=None     
# for i in range(-3,0):
#     if head==None:
#         head=n=Node(i)
#     else:
#         n.next=Node(i)
#         n=n.next 
# tail=n
# print_list(head)
# reverse(head)

#8. Delete a node in DLL basing on the key value
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
  
# def print_forwlist(t):
#     print("dll")
#     while(t):
#         print(t.data)
#         t=t.next

# def delete_at_position(t,k):
#     while(t.next!=None):
#         c=t
#         t=t.next
#         if t.data==k:
#             c.next=t.next
#             t.next.prev=c  
# head=None
# for i in range(6):
#     if head==None:
#         head=n=Node(i)
#     else:
#         n.next=Node(i)
#         n=n.next   
# tail=n        
# print_forwlist(head)
# delete_at_position(head,4)
# print_forwlist(head)  


#9. Delete a node in SLL basing on the position of the node
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
# del_inpos(head)
# print_list(head)

# #10 Merge two sorted lists to create a single sorted list
# class Node: 
#     def __init__(self, data): 
#         self.data = data 
#         self.next = None
  
  
# #Create & Handle List operations 
# class LinkedList: 
#     def __init__(self): 
#         self.head = None
  
#     # Method to display the list 
#     def printList(self): 
#         temp = self.head 
#         while temp: 
#             print(temp.data, end=" ") 
#             temp = temp.next
  
#     # Method to add element to list 
#     def addToList(self, newData): 
#         newNode = Node(newData) 
#         if self.head is None: 
#             self.head = newNode 
#             return
  
#         last = self.head 
#         while last.next: 
#             last = last.next
  
#         last.next = newNode 
  
  
# # Function to merge the lists 
# # Takes two lists which are sorted 
# # joins them to get a single sorted list 
# def mergeLists(headA, headB): 
  
#     # A dummy node to store the result 
#     dummyNode = Node(0) 
  
#     # Tail stores the last node 
#     tail = dummyNode 
#     while True: 
  
#         # If any of the list gets completely empty 
#         # directly join all the elements of the other list 
#         if headA is None: 
#             tail.next = headB 
#             break
#         if headB is None: 
#             tail.next = headA 
#             break
  
#         # Compare the data of the lists and whichever is smaller is 
#         # appended to the last of the merged list and the head is changed 
#         if headA.data <= headB.data: 
#             tail.next = headA 
#             headA = headA.next
#         else: 
#             tail.next = headB 
#             headB = headB.next
  
#         # Advance the tail 
#         tail = tail.next
  
#     # Returns the head of the merged list 
#     return dummyNode.next
  
  
# # Create 2 lists 
# listA = LinkedList() 
# listB = LinkedList() 
  
# # Add elements to the list in sorted order 
# listA.addToList(5) 
# listA.addToList(10) 
# listA.addToList(15) 
  
# listB.addToList(2) 
# listB.addToList(3) 
# listB.addToList(20) 
  
# # Call the merge function 
# listA.head = mergeLists(listA.head, listB.head) 
  
# # Display merged list 
# print("Merged Linked List is:") 
# listA.printList() 
  
#11. Implement a DLL by accepting the data to be stored into the linked list from user
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
#     l=int(input("value:"))
#     if head==None:
#         head=n=Node(l)
#     else:
#         t=n
#         n.next=Node(l)
#         n=n.next
#         n.prev=t 
# tail=n                
# print_forwlist(head)
# print_backlist(tail)

# 12.  Linear search on DLL
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
#         self.prev=None
# def print_list(t):
#     while(t):
#         print(t.data)
#         t=t.next
# def linear_search(t,p):
#     t=head
#     while (t!=None):
#         if t.data==p:
#             print("element found")
#             break
#         t=t.next
#     else :
#         print("element not found") 
# head=None
# for i in range(0,5):
#     if head==None:
#         head=n=Node(i)
#     else:
#         n.next=Node(i)
#         n.next.prev=n
#         n=n.next
# tail=n
# print_list(head)
# linear_search(head,4)

#13. Insert a new node basing on the key value. if key is found insert the new node after the key value.  if key value is not found add the new node at the end of the existing list

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

# def insert_atpos(t,pos):
#     n=Node(30)
#     while(t.next!=None):
#         if t.data==pos:
#             n.next=t.next
#             n.prev=t
#             t.next=n
#             n.next.prev=n
#         t=t.next    
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
# insert_atpos(head,3)
# print_forwlist(head)

# 14. Reverse the elements of the linked list

#       a. By swapping the values in the list without changing the links
# class Node:
#     def __init__(self, data):
#         self.prev=None
#         self.data = data
#         self.next = None
# def print_list(t):
#     while(t):
#         print(t.data)
#         t=t.next
# def reverse(t,k):
#     global m
#     for i in range(1,(m//2)+1):
#         if i==1:
#             t.data,k.data=k.data,t.data
#             t=t.next
#         else:

#             c=i
#             l=t
#             while c<=m-i-1:
#                 l=l.next
#                 c+=1
#             t.data,l.data=l.data,t.data 
#             t=t.next         
# head=None 
# m=int(input())       
# for i in range(1,m):
#     if head==None:
#         head=n=Node(i)
#     else:
#         n.next=Node(i)
#         n.next.prev=n
#         n=n.next
# tail=n
# print_list(head) 
# reverse(head,tail)
# print_list(head)  

#      b. By swapping the position of the nodes

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
#         self.prev=None
# def print_list(t):
#     while(t):
#         print(t.data)
#         t=t.next
# def reverse(t):
#     c=t
#     Next=None
#     Prev=None
#     while c:
#         Next = c.next
#         c.next =c.prev
#         c.prev=c
#         c=Next
#     head=Prev         
# head=None
# for i in range(0,5):
#     if head==None:
#         head=n=Node(i)
#     else:
#         n.next=Node(i)
#         n.next.prev=n
#         n=n.next
# tail=n
# print_list(head)
# reverse(head)
# print_list(tail)

#15. count the number of nodes in the list and print the list in reverse order
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
#         self.prev=None
# def print_list(t):
#     while(t):
#         print(t.data)
#         t=t.next
# def count(t) :
#     c=0
#     while(t!=None):
#         t=t.next
#         c+=1
#     print("the count is",c) 
# def reverse(t):
#     c=t
#     Next=None
#     Prev=None
#     while c:
#         Next = c.next
#         c.next =c.prev
#         c.prev=c
#         c=Next
#     head=Prev           
# head=None
# for i in range(0,5):
#     if head==None:
#         head=n=Node(i)
#     else:
#         n.next=Node(i)
#         n.next.prev=n
#         n=n.next
# tail=n
# print_list(head)
# count(head)
# reverse(head)
# print_list(tail)

#16. Create a DLL to store particulars of  students such as (rollno, name and branch) in each node. store atleast 4 students particulars
# class Node:
#     def __init__(self, name,rollno,branch):
#         self.prev=None
#         self.name = name
#         self.rollno=rollno
#         self.branch=branch
#         self.next = None
# def print_list(t):
#     while(t):
#         print(t.name,t.rollno,t.branch)
#         t=t.next         
# head=None
# for i in range(0,5):
#     x=int(input("roll"))
#     y=str(input("name"))
#     z=str(input("Branch"))
#     if head==None:
#         head=n=Node(x,y,z)
#     else:
#         n.next=Node(x,y,z)
#         n.next.prev=n
#         n=n.next
# print_list(head)     

#17. create a DLL list in reverse order i.e store None in the first node and let the second node have the address of the first node.  store the address of the last node in header node.
# class Node:
#     def __init__(self, data):
#         self.prev = None
#         self.data = data
#         self.next = None
# def print_list(t):
#     while(t):
#         print(t.data)
#         t=t.next
# def reverse(t):
#     print("dll")
#     for i in range(1,5):
#         global head
#         t=head
#         c=0
#         while c+i<4:
#             t=t.next
#             c+=1
#         print(t.data)    

# head=None
# for i in range(1,5):
#     if head==None:
#         head=n=Node(i)
#     else:
#         n.next=Node(i)
#         n.next.prev=n
#         n=n.next
# tail=n
# print_list(head)
# reverse(head)

#18. Delete a node in DLL basing on the key value
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

# def delete_at_position(t,k):
#     while(t.next!=None):
#         c=t
#         t=t.next
#         if t.data==k:
#             c.next=t.next
#             t.next.prev=c  
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
# delete_at_position(head,4)
# print_forwlist(head)  

#19. Delete a node in DLL basing on the position of the node
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
# delete_at_position(head)
# print_forwlist(head)  

# #20 Merge two sorted  dll lists to create a single sorted list
# class Node: 
#     def __init__(self, data): 
#         self.prev = None
#         self.data = data 
#         self.next = None
  
  
# #Create & Handle List operations 
# class LinkedList: 
#     def __init__(self): 
#         self.head = None
  
#     # Method to display the list 
#     def printList(self): 
#         temp = self.head 
#         while temp: 
#             print(temp.data, end=" ") 
#             temp = temp.next
  
#     # Method to add element to list 
#     def addToList(self, newData): 
#         newNode = Node(newData) 
#         if self.head is None: 
#             self.head = newNode 
#             return
  
#         last = self.head 
#         while last.next: 
#             last = last.next
  
#         last.next = newNode 
  
  
# # Function to merge the lists 
# # Takes two lists which are sorted 
# # joins them to get a single sorted list 
# def mergeLists(headA, headB): 
  
#     # A dummy node to store the result 
#     dummyNode = Node(0) 
  
#     # Tail stores the last node 
#     tail = dummyNode 
#     while True: 
  
#         # If any of the list gets completely empty 
#         # directly join all the elements of the other list 
#         if headA is None: 
#             tail.next = headB 
#             break
#         if headB is None: 
#             tail.next = headA 
#             break
  
#         # Compare the data of the lists and whichever is smaller is 
#         # appended to the last of the merged list and the head is changed 
#         if headA.data <= headB.data: 
#             tail.next = headA 
#             headA = headA.next
#         else: 
#             tail.next = headB 
#             headB = headB.next
  
#         # Advance the tail 
#         tail = tail.next
  
#     # Returns the head of the merged list 
#     return dummyNode.next
  
  
# # Create 2 lists 
# listA = LinkedList() 
# listB = LinkedList() 
  
# # Add elements to the list in sorted order 
# listA.addToList(5) 
# listA.addToList(10) 
# listA.addToList(15) 
  
# listB.addToList(2) 
# listB.addToList(3) 
# listB.addToList(20) 
  
# # Call the merge function 
# listA.head = mergeLists(listA.head, listB.head) 
  
# # Display merged list 
# print("Merged Linked List is:") 
# listA.printList() 