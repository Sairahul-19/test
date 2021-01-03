#single linked lists

# 1. write a program to search for an element in a sll.(linera search)if the element is found print its location otherwise print element not found
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
# linear_search(head,7)   

#5. Program to insert an element after a given value in an SLL
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

#6. Program to reverse all the nodes in a SLL
#    Test Case1:
#     I/P: 
#        1->2->3->4->None
#     O/P:
#        4->3->2->1->None

  # b. Shift the nodes(relocate) for reversing(modify the addresses)
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

#    a. by swapping the values in the SLL without relocating the nodes

#method 1
# class Node:
#     def _init_(self, data):
#         self.data = data
#         self.next = None
# def print_list(t):
#     while(t):
#         print(t.data)
#         t=t.next
# def reverse(t,k):
#     for i in range(1,2):
#         t.data,k.data=k.data,t.data
#         t=t.next
#         k=t.next
# head=None        
# for i in range(1,5):
#     if head==None:
#         head=n=Node(i)
#     else:
#         n.next=Node(i)
#         n=n.next 
# tail=n
# print_list(head) 
# reverse(head,tail)
# print_list(head)

#method 2
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

#7. Program to sort the elements in a SLL
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def sort(t):
    c=None
    for i in range(0,4):
      while(t.next!=None):
          c=t.next
          if t.data > c.data:
              temp=t.data
              t.data=c.data
              c.data=temp
          t=t.next
def print_list(t):
    while(t):
        print(t.data)
        t=t.next
head=None
for i in range(0,4):
    l=int(input())
    if head==None:
        head=n=Node(l)
    else:
        n.next=Node(l)
        n=n.next
sort(head)
print("after sorting is ")
print_list(head)


#8. Program to create an SLL in Reverse order
	#None<-1<-2<-3
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