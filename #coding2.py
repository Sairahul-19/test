#coding2
#write program to find the factorial of a given number
#a. Without using a Function
n=int(input())
f=1
for i in range(1,n+1):
    f*=i

print(f) 
#b. Uing a function
def fact(n):
    s=1
    for i in range(1,n+1):
        s*=i
    print(s)
fact(6)        
 #c. using a recursive function

def fac(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fac(n-1) 
print(fac(3)) 

#loop without using recursion find fibanocci
a=int(input("Enter the first number of the series "))
b=int(input("Enter the second number of the series "))
n=int(input("Enter the number of terms needed "))
print(a,b,end=" ")
while(n-2)>=0:
    c=a+b
    a=b
    b=c
    print(c,end=" ")
    n=n-1

n=int(input())
while n>=0:
    s=[]
    if i==1 or i==2:
        r=1
    else:    
        r=(n-1)+(n-2)
    s.append(r)
for i in s:
    print(s)  

#use recursion and verify the time taken
n=int(input())
def fibonacci(n):
    if n==1:
        return 1
    elif n==2:
        return 1    
    elif n>2:
        return (fibonacci(n-1)+fibonacci(n-2))

for i in range(1,n):
    print(fibonacci(i))  
#using of concept of memoization
cache={}
def fab(N):
    if N in cache:
        return cache[N]
    elif N==0 or N==1:
        return N    
    else :
        value= (fab(N-1)+fab(N-2))
    cache[N]=value
    return value
for i in range(1,110):
    print(i,":",fab(i)) 
    
#program to search a elementin a sorted list using recursion     
     
lst=[1,2,3,4,5,6,7,8,9]
def search(l,n,x):
    if(n<l):
        return -1
    elif lst[l]==x:
        return 1
    elif lst[n]==x:
        return 1
    else :
        return search(l+1,n-1,x)
se=int(input('number'))
l=0
n=len(lst)-1
s=search(l,n,se)
if s!=-1:
    print('element found')
else:
    print('not found')
    
# binary search
lst=[1,2,3,4,5,6,7,8,9]
def binary_search(arr,x,low,high):
    if(low>=high):
        return False
    else:
        mid=(low+high)//2
        if arr[mid]==x:
            return True
        elif arr[mid]>x:
            return binary_search(arr,x,low,mid-1)
        else :
            return binary_search(arr,x,mid+1,high)
print(binary_search(lst,7,0,len(lst)))


alist=[1,2,3,4,5,6,7,8,9]
key=int(input())
start = 0

end = len(alist)
while start < end:
    mid = (start + end)//2
    if mid==key:
       
        print("element is found")
        break
    elif alist[mid] > key:
        end = mid
    elif alist[mid] < key:
        start = mid + 1
    else:
        print("element not found")


lst6=[1,45,3,455,22,43,21,7,68,9] 
print(lst6)
min=0
for i in range(len(lst6)):
    for j in range(i+1,len(lst6)):
        if lst6[i]>lst6[j]: 
           min=lst6[j]
           lst6[j]=lst6[i]
           lst6[i]=min

print(lst6)          

#liner sort       
lst7=[1,45,3,455,22,43,21,7,68,9] 
print(lst7)
min=0
for i in range(len(lst7)):
    for j in range(len(lst7)-1):
        if lst7[j]>lst7[j+1]: 
           min=lst7[j+1]
           lst7[j+1]=lst7[j]
           lst7[j]=min

print(lst7) 

# bubble sort
lst8=[13,4,6,2,44] 
print(lst8)

for i in range(len(lst8)):
    for j in range(len(lst8)-1):
        if lst8[j]>lst8[j+1]:
            lst8[j],lst8[j+1]=lst8[j+1],lst8[j]
           
print(lst8) 

# insertion sort
lst9=[10,8,5,20,19,6,3] 
print(lst9)
for i in range(1, len(lst9)):   
        key = lst9[i] 
        j = i-1
        while j >=0 and key < lst9[j] : 
                lst9[j+1] = lst9[j] 
                j -= 1
        lst9[j+1] = key           
print(key)  
                                       





