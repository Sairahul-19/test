#evaluate a given postfix expression
# class evaluate_postfix:
#     def __init__(self):
#         self.items=[]
#         self.size=-1
#     def isEmpty(self):
#         return self.items==[]
#     def push(self,item):
#         self.items.append(item)
#         self.size+=1
#     def pop(self):
#         if self.isEmpty():
#             return 0
#         else:
#             self.size-=1
#             return self.items.pop()

#     def evalute(self,expr):
#         for i in expr:
#             if i in '0123456789':
#                 self.push(i)
#             else:
#                 op1=self.pop()
#                 op2=self.pop()
#                 result=self.cal(op2,op1,i)
#                 self.push(result)
#         return self.pop()
#     def cal(self,op2,op1,i):
#         if i == '*':
#             return int(op2)*int(op1)
#         elif i == '/':
#             return int(op2)/int(op1)
#         elif i == '+':
#             return int(op2)+int(op1)
#         elif i == '-':
#             return int(op2)-int(op1)
#         elif i == '^':
#             return int(op2)**int(op1)   
# s=evaluate_postfix()
# expr=input('enter the postfix expression')
# value=s.evalute(expr)
# print('the result of postfix expression',expr,'is',value)

#infix to prefix
# class infix_to_prefix:
#     precedence={'^':5,'*':4,'/':4,'+':3,'-':3,'(':2,')':1}
#     def __init__(self):
#         self.items=[]
#         self.size=-1
#     def push(self,value):
#         self.items.append(value) 
#         self.size+=1
#     def pop(self):
#         if self.isempty():
#             return 0
#         else:
#             self.size-=1
#             return self.items.pop()
#     def isempty(self):
#         if(self.size==-1):
#             return True
#         else:
#             return False
#     def seek(self):
#         if self.isempty():
#             return False
#         else:
#             return self.items[self.size]
#     def is0perand(self,i):
#         if i.isalpha() or i in '1234567890':
#             return True
#         else:
#             return False
#     def reverse(self,expr):
#         rev=""
#         for i in expr:
#             if i is '(':
#                 i=')'
#             elif i is ')':
#                 i='('
#             rev=i+rev
#         return rev
#     def infixtoprefix (self,expr):
#         prefix=""
#         for i in expr:
#             if(len(expr)%2==0):
#                 print("Incorrect infix expr")
#                 return False
#             elif(self.is0perand(i)):
#                 prefix +=i
#             elif(i in '+-*/^'):
#                 while(len(self.items)and self.precedence[i] < self.precedence[self.seek()]):
#                     prefix+=self.pop()
#                 self.push(i)
#             elif i is '(':
#                 self.push(i)
#             elif i is ')':
#                 o=self.pop()
#                 while o!='(':
#                     prefix +=o
#                     o=self.pop()
#                 #end of for
#         while len(self.items):
#             if(self.seek()=='('):
#                 self.pop()
#             else:
#                 prefix+=self.pop()
#         return prefix        
# s=infix_to_prefix()
# expr=input('enter the expression ')
# rev=""
# rev=s.reverse(expr)
# #print(rev)
# result=s.infixtoprefix(rev)
# if (result!=False):    
#     prefix=s.reverse(result)
#     print("the prefix expr of :",expr,"is",prefix)

#infix to postfix
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

#evaluate the prefix expression
# class evaluate_prefix:
#     def __init__(self):
#         self.items=[]
#         self.size=-1
#     def isEmpty(self):
#         if(self.size==-1):
#             return True
#         else:
#             return False
#     def push(self,item):
#         self.items.append(item)
#         self.size+=1
#     def pop(self):
#         if self.isEmpty():
#             return 0
#         else:
#             self.size-=1
#             return self.items.pop()
#     def seek(self):
#         if self.isEmpty():
#             return False
#         else:
#             return self.items[self.size]
#     def evalute(self,expr):
#         for i in reversed(expr):
#             if i in '0123456789':
#                 self.push(i)
#             else:
#                 op1=self.pop()
#                 op2=self.pop()
#                 result=self.cal(op1,op2,i)
#                 self.push(result)
#         return self.pop()
#     def cal(self,op1,op2,i):
#         if i is '*':
#             return int(op1)*int(op2)
#         elif i is '/':
#             return int(op1)/int(op2)
#         elif i is '+':
#             return int(op1)+int(op2)
#         elif i is '-':
#             return int(op1)-int(op2)
#         elif i is '^':
#             return int(op1)^int(op2)
# s=evaluate_prefix()
# expr=input('enter the prefix expression')
# value=s.evalute(expr)
# print('the result of postfix expression',expr,'is',value)

 #leap year
# year = int(input('enter the year'))

# if((year%4==0) and (year%100!=0)):
#     print('leap year')
# elif year%100==0:
#     print('leap year')
# elif year%400==0:
#     print('leap year')        
# else:
#     print('not a leap year') 


# owners browsing bill

# H=float(input('enter the hours'))
# C=0
# if(H==1):
#     C=20
#     print(C)
# elif(H==0.5):
#     C=10
#     print(C)
# elif(H>1 and H<=10):
#     C=20*H
#     print(C)
# elif(H>10):
#     print('unlimited') 
#     c=100
#     print(c)

#print the activity
# temp=['warm','cool']  
# humidity=['dry','humid']  
# n=str(input('enter temp'))
# m=str(input('enter humidity'))

# if(n=='warm'):
        
#      if(m=='dry'):
#         print('play basketball')
#      else:
#         print    ('play tennis')
# else:
        
#     if(m=='dry'):
#         print('play cricket')
#     else:
#         print('swim')

#significant digits
# i=int(input('enter the number'))
# s=0
# if(i%10==5):
#     s=i*i
#     print(s)

#enrol a student
# age=int(input('enter the age'))

# if not (age>15 and age<18):
#     print('student is not enrolled')
# else:
#     print('student is  enrolled')

#prints sequence of powers

# n=int(input('enter the number'))  
# m=n+1
# for i in range(m):
#     print(5**i)

# print('kilo-gram')
# for i in range(1,4):
#  print(i,'-',i*1000)


a=0
ds=0
ws=0
d=0
while True:
    while d !=7:
        d+=1
        c1=float(input('enter the price:'))
        c2=float(input('enter the price:'))
        c3=float(input('enter the price:'))
        c4=float(input('enter the price:'))
        c5=float(input('enter the price:'))
        ds+=c1+c2+c3+c4+c5
        ws+=ds
        print('day sum',ds)

    break
print(round(ws,2))








