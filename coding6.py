#deleting of entire lists
#method 1
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
# def delete(t,k):
#     global head
#     global tail
#     t=head
#     k=tail
#     for i in range(0,6):
#         if i==5:
#             print('The deleted element is',tail.data)
#             tail.prev=None
#             tail.next=None
#             del k
#             del t
#             tail=None
#             head =None
#         else:    
#             print('The deleted element is',head.data)
#             del t
#             head=head.next
#             head.prev=None
#             t=head
       

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
# print_dll(head)
# delete(head,tail)
# print_dll(head)

# #method 2
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
#         self.prev=None
# def print_list(t):
#     print("the data in dll")
#     while(t):
#         print(t.data)
#         t=t.next
# def delete_all(q):
#     while(q.next!=None):
#         t=q
#         q=q.next
#         c=t.next
#         c.prev=None
#         t.next=None
#     global head
#     head=None
#     global tail 
#     tail=None
#     global n 
#     n=None
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
# delete_all(head)
# print_list(head)

# Counting total number of nodes.

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

# Searching an item in list.

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

# Reversing the list

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

