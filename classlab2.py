# # binary search
# alist=[1,2,3,4,5,6,7,8,9]
# key=int(input())
# start = 0
# end = len(alist)
# while start < end:
#     mid = (start + end)//2
#     if alist[mid]==key:       
#       print("element is found")
#       break
#     elif alist[mid] > key:
#       end = mid - 1
#     elif alist[mid] < key:
#       start = mid + 1
#     else:
#       print("element not found")
#       break

# #selecction sorted
# print("selection sort")
# lst10=[10,8,5,20,19,6,3] 
# for i in range(len(lst10)):
#   mini=i
#   for j in range(i+1,len(lst10)):
#     if lst10[mini]>lst10[j]:
#       mini=j
#   lst10[i],lst10[mini]= lst10[mini],lst10[i]
#   print(lst10)
# #insertion sort
# print("insertion sort")
# lst9=[10,8,5,20,19,6,3] 
# print(lst9)
# for i in range(1, len(lst9)):
#     j=i-1
#     while j>=0:
#         if(lst9[j]>lst9[j+1]):
#             lst9[j+1],lst9[j]=lst9[j],lst9[j+1]
#         j-=1    
# print(lst9) 
# #linear search
# print("linear search")
# lst6=[1,45,3,455,22,43,21,7,68,9] 
# print(lst6)
# key=int(input())
# f=0
# for i in range(len(lst6)):
#   if key==lst6[i]:
#     f=1
#     break
#   else:
#     f=-1
# if f==1:
#   print("element found") 
# else:
#   print("element not found")  

# #bubble Sort
# print("bubble sort")
# lst8=[13,4,6,2,44] 
# print(lst8)

# for i in range(len(lst8)):
#     for j in range(len(lst8)-1):
#         if lst8[j]>lst8[j+1]:
#             lst8[j],lst8[j+1]=lst8[j+1],lst8[j]
           
# print(lst8) 

# # armstrong number
# num = int(input("Enter a number: "))

# s = 0

# y = num
# while y > 0:
#    digit = y % 10
#    s += digit ** 3
#    y//= 10

# if num == s:
#    print("True")
# else:
#    print("false")

# Q2. Given a list of integers nums, return whether there's an integer 
# whose frequency in the list is same as its value.

# Example 1
# Input

# nums = [7, 9, 3, 3, 3]
# Output

# True
# Explanation

# The number 3 appears 3 times

# nums=[7,9,3,3,3]
# m=0
# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         if nums[i]==nums[j]:
#             m=nums[i]
# print(m)
# if m==nums.count(m):
#     print("True")
# else:
#     print("False") 
#model 2
# l=list(map(int,input('Enter the elements in one line: ').split()))
# for i in set(l):
#     if i==l.count(i):
#         print('True')
#         break
# else:
#     print('False')    

# You are given a two-dimensional list of integers intervals and an integer point. Each element contains [start, end] represents an inclusive interval.

# Return the number of intervals that are intersecting at point.

# Example 1
# Input

# intervals = [
#     [1, 5],
#     [3, 9],
#     [4, 8],
#     [10, 13]
# ]
# point = 4
# Output

# 3
# Explanation

# At time 4, there were 3 programmers working [1, 5], [3, 9], [4, 8]    

# n=int(input('Enter the point: '))
# s=0
# for i in range(int(input('Enter the number of ranges: '))):
#     l=list(map(int,input("enter the lower and upper limit in single line: ").split()))
#     if n in range(l[0],l[1]+1):
#         s+=1
# print(s)

