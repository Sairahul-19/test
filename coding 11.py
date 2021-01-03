#perform a program in binary order in inorder traversal
# class TreeNode:
#    def __init__(self, data, left = None, right = None):
#       self.data = data
#       self.left = left
#       self.right = right
# def insert(temp,data):
#    que = []
#    que.append(temp)
#    while (len(que)):
#       temp = que[0]
#       que.pop(0)
#       if (not temp.left):
#          temp.left = TreeNode(data)
#          break
#       else:
#          que.append(temp.left)
#       if (not temp.right):
#          temp.right = TreeNode(data)
#          break
#       else:
#          que.append(temp.right)
# def make_tree(elements):
#    Tree = TreeNode(elements[0])
#    for element in elements[1:]:
#       insert(Tree, element)
#    return Tree

# class Solution(object):
#    def inorderTraversal(self, root):
#       res, stack = [], []
#       current = root
#       while True:
#          while current:
#             stack.append(current)
#             current = current.left
#          if len(stack) == 0:
#             return res
#          node = stack[-1]
#          stack.pop(len(stack)-1)
#          if node.data != None:
#             res.append(node.data)
#          current = node.right
#       return res
# ob1 = Solution()
# root = make_tree([10,5,15,2,7,None,20])
# print(ob1.inorderTraversal(root))

class Tree:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
def insert(root, key): 
    if root is None: 
        return Tree(key) 
    else: 
        if root.data == key: 
            return root 
        elif root.data < key: 
            root.right = insert(root.right, key) 
        else: 
            root.left = insert(root.left, key) 
    return root 
  


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

def preorder(root):
    if root:
        print(root.data)
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data) 

def search(root,key):
    if root is None:
        return None
    elif root.data==key:
        return True                   
    if root.data < key: 
        return search(root.right,key) 
    else:
        return search(root.left,key) 

r = Tree(5) 
r = insert(r, 3) 
r = insert(r, 2) 
r = insert(r, 4) 
r = insert(r, 7) 
r = insert(r, 6) 
r = insert(r, 8) 
# m=int(input())
# r=Tree(int(input()))
# for i in range(m):
#     r=insert(r,int(input()))

print(' in-order traversal of the BST ')
inorder(r) 

print(' pre-order traversal of the BST ')
preorder(r)

print(' post-order traversal of the BST ')
postorder(r)

k=int(input('Enter search element'))
r=search(r,k)
if r==None:
    print('search Element is Not found')
else:
    print('Search element is found')


#Write a program to convert the infix expression into postfix form.
# class stack:
#     def __init__(self):
#         self.stack=[]
#         self.top=-1
#     def isEmpty(self):
#         if self.top==-1:
#             return True      
#     def inFixToPostFix(self):
#         postFix=''
#         global inFix
#         for c in inFix:
#             # if elif chain for anything that c can be
#             if c in "0123456789x":
#                 postFix += c
#             elif c in "+-":
#                 if self.Stack.isEmpty():
#                     self.Stack.push(c)
#                 elif self.Stack.top() =='(':
#                     self.Stack.push(c)
#             elif c in "*/":
#                 if self.Stack.isEmpty():
#                     self.Stack.push(c)
#                 elif self.Stack.top() in "+-(":
#                     self.Stack.push(c)
#             elif c == "(":
#                 self.Stack.push(c)
#             elif c == ")":
#                 while self.Stack.top() != '(':
#                     postFix += self.Stack.pop()
#                 self.Stack.pop()
#             else:
#                 print("Error")
#         print(postFix)
#         return postFix 
#     # def isEmpty(self):
#     #     if self.top==-1:
#     #         return True    
# s=stack()
# inFix='1+2*(3-4)/5/6'
# for i in inFix:
#     s.stack.append(i)
#     s.top+=1
# s.inFixToPostFix() 

#method-2
# OPERATORS = set(['+', '-', '*', '/', '(', ')', '^'])  # set of operators
# PRIORITY = {'+':1, '-':1, '*':2, '/':2, '^':3} # dictionary having priorities 
# def infix_to_postfix(expression): #input expression
#     stack = [] # initially stack empty
#     output = '' # initially output empty
#     for ch in expression:
#         if ch not in OPERATORS:  # if an operand then put it directly in postfix expression
#             output+= ch
#         elif ch=='(':  # else operators should be put in stack
#             stack.append('(')
#         elif ch==')':
#             while stack and stack[-1]!= '(':
#                 output+=stack.pop()
#             stack.pop()
#         else:
#             # lesser priority can't be on top on higher or equal priority    
#              # so pop and put in output   
#             while stack and stack[-1]!='(' and PRIORITY[ch]<=PRIORITY[stack[-1]]:
#                 output+=stack.pop()
#             stack.append(ch)
#     while stack:
#         output+=stack.pop()
#     return output
# expression = input('Enter infix expression')
# print('infix expression: ',expression)
# print('postfix expression: ',infix_to_postfix(expression))



#Write a program to create a Circular singly linked list for adding and deleting a Node.
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
#     c=1
#     while(c < pos):
#         t = t.next
#         c += 1
#     n.next=t.next
#     t.next=n
# def delete(t,pos): 
#     c=1
#     while(c < pos):
#         n=t
#         t = t.next
#         c += 1
#     n.next=t.next    

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
# delete(head,3)
# print_list(head)


