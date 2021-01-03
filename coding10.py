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

# #method2
# class postfix:
#     def __init__(self):
#         self.res=[]
#         self.top=-1
#     def push(self,c):
#         self.res.append(c)
#         self.top+=1
#     def pop(self):
#         if self.top==-1:
#             print('the res is empty') 
#         else:
#             self.top-=1
#             self.res.pop()
#     def display(self):
#         print('result',self.res)
# st=str(input("enter a postfix"))
# S=postfix()
# for i in st:
#     if i=='+':
#         a=S.pop()
#         b=S.pop()
#         c=a+b
#         S.push(c)
#     elif i=='-':
#         a=S.pop()
#         b=S.pop()
#         try:
#          c=b-a
#          S.push(c)
#         except:
#             print()
#     elif i=='*':
#         a=S.pop()
#         b=S.pop()
#         try:
#          c=a*b
#          S.push(c)
#         except:
#             print()
#     elif i=='/':
#         a=S.pop()
#         b=S.pop()
#         c=b/a
#         S.push(c)
#     elif i=='^':
#         a=S.pop()
#         b=S.pop()
#         c=b**a
#         S.push(c)
#     else:
#         S.push(i)
# S.display() 

#evaluate the given prefix expression                  
class prefix:
    def __init__(self):
        self.res=[]
        self.top=-1
    def push(self,c):
        self.res.append(c)
        self.top+=1
    def pop(self):
        if self.top==-1:
            print('the res is empty') 
        else:
            self.top-=1
            self.res.pop()
    def display(self):
        print('result',self.res)
st=str(input("enter a prefix"))
S=prefix()

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
 