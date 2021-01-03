#1.Write a program to find the max element of an array and swap it with the last unsorted value of the array.

# a=[10,8,5,20,19,6,3]
# for i in range(len(a)):
#     maxi=a.index(max(a[:len(a)-i]))  
#     if maxi==len(a)-i:
#       a[maxi]==a[len(a)-i]
#     else:
#       a[len(a)-1-i],a[maxi]=a[maxi],a[len(a)-1-i]
#     print(a) 

#2. write a program to find the reverse of a given number without any loops.
# rev=0
# def reverse(v):
#     global rev
#     if v>0:
#         rem=v%10
#         rev=rev*10+rem
#         reverse(v//10)
#     return rev
# x=int(input('enter a number'))
# z=reverse(x)
# print(z)
#3.  Reverse the array with using loops
# arr1=[1,2,3,4,5,6]
# n=len(arr1)-1
# for i in range(0,len(arr1)//2):
#     arr1[i],arr1[n-i]=arr1[n-i],arr1[i]
# print(arr1)
#4.  Find the maximum and minimum element in an array
# l=[1,5,4,6,7,8,0,9]
# mini=l[0]
# maxi=l[len(l)-1]
# for i in range(0,len(l)-1):
#     if l[i]<mini or l[i]>maxi:
#         if l[i]<mini:
#             mini=l[i]
#         else:
#             maxi=l[i]
# print(mini)
# print(maxi)
#5.  Find the "Kth" max and min element of an array 
# k=int(input())
# lst7=[3,5,2,5,19,12,9,4]
# for i in range(len(lst7)):
#     for j in range(len(lst7)-1):
#         if lst7[j]>lst7[j+1]: 
#            min=lst7[j+1]
#            lst7[j+1]=lst7[j]
#            lst7[j]=min
# print(lst7[k-1],"as kth minimum")
# print(lst7[len(lst7)-k],"as kth maximum")           

#6.  Given an array which consists of only 0, 1 and 2. Sort the array without using any sorting algo.
# l=[0,1,2,2,1,0,0,1,2]
# l0=[]
# l1=[]
# l2=[]
# l3=[]
# for i in range(len(l)):
#     if l[i]==0:
#         l0.append(l[i])
#     elif l[i]==1:
#         l1.append(l[i])
#     else:
#         l2.append(l[i])
# l3=l0+l1+l2
# print(l3)
#7.  Move all the negative elements to one side of the array 
# lst=[1,2,3,-4,-6,-2,9,6,7,8]
# j=0
# for i in range(len(lst)):  
#     if lst[i]<0:
#         lst[i],lst[j]=lst[j],lst[i]
#         j+=1
# print(lst)            

#8.  Find the Union and Intersection of the two sorted arrays
# lst1=[1,2,3,4,5,6,7,8]
# lst2=[8,5,7,0,3,7,8,9]
# lst1=sorted(lst1)
# lst2=sorted(lst2)
# lst3=lst1+lst2
# n=len(lst3)
# lst4=[]
# lst5=[]
# for i in range(n):
#     j=i+1
#     while j<n:
#         if lst3[i]==lst3[j]:
#             lst4.append(lst3[j])
#             lst3.pop(j)
#             n-=1
#         j+=1
# lst4=list(set(lst4))
# lst3=list(set(lst3))
# print(lst4,"is intersection")
# print(lst3,"is union")  
#method 2
# lst1=[1,2,3,3,4,5]
# lst2=[1,2,3,3,3,3,3,3,3,6,8]
# lst3=lst1+lst2
# n=len(lst3)
# lst4=[]
# lst5=[]
# for i in range(n):
#     j=i+1
#     while j<n:
#         if lst3[i]==lst3[j]:
#             lst4.append(lst3[j])
#             lst3.pop(j)
#             n-=1
#         j+=1
# for i in range(len(lst4)):
#     for j in range(len(lst4)-1):
#         if lst4[j]>lst4[j+1]: 
#            lst4[j+1],lst4[j]=lst4[j],lst4[j+1]
# for i in lst4:        
#     while i in lst4[i:]:
#         lst4.remove(i)                                         
# for i in range(len(lst3)):
#     for j in range(len(lst3)-1):
#         if lst3[j]>lst3[j+1]: 
#            lst3[j+1],lst3[j]=lst3[j],lst3[j+1]  
# for i in lst3:        
#     while i in lst3[i:]:
#         lst3.remove(i)
# print(lst4,"is intersection")
# print(lst3,"is union") 
  

#9 write a program to cyclically rotate an array by one
# arr=[1,2,3,4,5]
# n=len(arr)
# x = arr[n - 1]       
# for i in range(n - 1, 0, -1): 
#     arr[i] = arr[i - 1];           
# arr[0] = x
# print(arr)

# #10 find largest sum contigous subarray
arr1=[-1,-2,-3,-4]
arr2=[]
n=len(arr1)
l=0
for i in range(n):
    l+=arr1[i]
    if l<0:
        print(l)
    elif arr1[i]<0 or arr1[i]>0 :
        if arr1[i+1]>0 and arr1[i+2]>0:
            if arr1[n-1]<0:
                arr1.pop(n-1)
                n-=1
            if arr1[i]<0:
                for j in range(i+1,n):
                    arr2.append(arr1[j])
            else:
                for j in range(i,n):
                    arr2.append(arr1[j])

            break
                        
print(arr2)
s=0
for i in arr2:
    s+=i
print(s,"sum of contigous subarray")  

#11 minimise the maximum difference between heights

#12 minimum no.of jumps to reach end of an array
#13 find duplicates in an array of N+1 integers
#14 merge two sorted arrays without using extra place

#8th questiom 3rd method
# lst1=[1,2,3,33,3,4,5,6]
# lst2=[1,2,3,3,3,3,5,68,12]
# lst1=sorted(lst1)
# lst2=sorted(lst2)
# lst3=lst1+lst2
# n=len(lst3)
# lst4=[]
# lst5=[]
# for i in range(n):
#     j=i+1
#     while j<n:
#         if lst3[i]==lst3[j]:
#             lst4.append(lst3[j])
#             lst3.pop(j)
#             n-=1
#         j+=1
# m=len(lst4)        
# for i in range(m):
#     j=i+1
#     while j<m:
#         if lst4[i]==lst4[j]:
#             lst4.pop(j)
#             m-=1
#         j+=1
# for i in range(len(lst4)):
#     for j in range(len(lst4)-1):
#         if lst4[j]>lst4[j+1]: 
#            lst4[j+1],lst4[j]=lst4[j],lst4[j+1]         
# l=len(lst3)        
# for i in range(l):
#     j=i+1
#     while j<l:
#         if lst3[i]==lst3[j]:
#             lst3.pop(j)
#             l-=1
#         j+=1            
# for i in range(len(lst3)):
#     for j in range(len(lst3)-1):
#         if lst3[j]>lst3[j+1]: 
#            lst3[j+1],lst3[j]=lst3[j],lst3[j+1]  
# n4=len(lst4)
# for i in range(n4):
#     for j in range(n4):
#         if i==j:
#             continue
#         elif lst4[i]==lst4[j]:
#             lst4.pop(j)
#             lst4.insert(n4,'x')
# while 'x' in lst4:
#     lst4.remove('x')
# print(lst4,"is intersection")
# n3=len(lst3)
# for i in range(n3):
#     for j in range(n3):
#         if i==j:
#             continue
#         elif lst3[i]==lst3[j]:
#             lst3.pop(j)
#             lst3.insert(n3,'x')
# while 'x' in lst3:
#     lst3.remove('x')
# print(lst3,"is union")
              




