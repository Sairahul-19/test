# write a program to do perform the following:
# 1. Insert an element basing on key in a circularly linked sll
# 2. Insert an element basing on key in a circularly linked DLL
# 3. Delete an element basing on the key in a Circularly linked SLL
#4. Delete an element basing on the key in a circularly linked DLL

# 1. Insert an element basing on key in a circularly linked sll

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None

# # print the elements in the csll
# def print_list(n):

#     print('The lement in the Circularly linked list are:')
#     print(n.data)
#     n=n.next
#     while(n!=head):
#         print(n.data)
#         n=n.next
# def insert(t,pos): 
#     n=Node(30)
#     while(t.next!=head):
#         if t.data==pos:
#             n.next=t.next
#             t.next=n
#         t=t.next
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
# print_list(head)
# insert(head,3)
# print_list(head)

# 2. Insert an element basing on key in a circularly linked DLL

class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None
def print_list(n):
    print('The lement in the Circularly linked list are:')
    print(n.data)
    n=n.next
    while(n!=head):
        print(n.data)
        n=n.next
def prt_list(n):
    print('The lement in the Circularly linked list are:')
    print(n.data)
    n=n.prev
    while(n!=tail):
        print(n.data)
        n=n.prev  
def insert(t,pos):
    n=Node(30)
    while(t.next!=head):
        if t.data==pos:
            n.next=t.next
            n.prev=t
            t.next=n
            n.next.prev=n
        t=t.next                   
head=None
for i in range(0,5):
    if head==None:
        head=n=Node(i)
    else:
        n.next=Node(i)
        n.next.prev=n
        n=n.next
tail=n
tail.next=head
head.prev=tail  
print_list(head)
prt_list(tail) 
insert(head,3)  
print_list(head)
prt_list(tail)   

# 3. Delete an element basing on the key in a Circularly linked SLL
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None

# # print the elements in the csll
# def print_list(n):
#     print('The lement in the Circularly linked list are:')
#     print(n.data)
#     n=n.next
#     while(n!=head):
#         print(n.data)
#         n=n.next
# def delete(t,pos):
#     while(t.next!=head):
#         c=t
#         t=t.next
#         if t.data==pos:
#             c.next=t.next
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
# print_list(head)
# delete(head,3)
# print_list(head)

#4. Delete an element basing on the key in a circularly linked DLL

# class Node:
#     def __init__(self,data):
#         self.prev=None
#         self.data=data
#         self.next=None
# def print_list(n):
#     print('The lement in the Circularly linked list are:')
#     print(n.data)
#     n=n.next
#     while(n!=head):
#         print(n.data)
#         n=n.next
# def prt_list(n):
#     print('The lement in the Circularly linked list are:')
#     print(n.data)
#     n=n.prev
#     while(n!=tail):
#         print(n.data)
#         n=n.prev  
# def delete(t,pos):
#     while(t.next!=head):
#         c=t
#         t=t.next
#         if t.data==pos:
#             c.next=t.next
#             t.next.prev=c     
# head=None
# for i in range(0,5):
#     if head==None:
#         head=n=Node(i)
#     else:
#         n.next=Node(i)
#         n.next.prev=n
#         n=n.next
# tail=n
# tail.next=head
# head.prev=tail  
# print_list(head)
# prt_list(tail) 
# delete(head,3)  
# print_list(head)
# prt_list(tail)  


