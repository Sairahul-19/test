#coding 3
#shift the array manually without using insert and also do not pop the element simply overwrite it


#model 1
#it will take input and copied in list l
l=list(map(int,input().split()))
for i in range(1,len(l)):
  for j in range(i):
    if l[i]<l[j]:
      l.insert(j,l[i])
      l.pop(i+1)
      break
print(l)
#model 2
lst9=[10,8,5,20,19,6,3] 
print(lst9)
#it takes i from 1-len-1
for i in range(1, len(lst9)):   
        key = lst9[i] 
        j = i-1
        #it will happens run till the element comes to its ascending order position
        while j >=0 and key < lst9[j] : 
                lst9[j+1] = lst9[j] 
                j -= 1
        lst9[j+1] = key           
print(lst9)
#
lst9=[10,8,5,20,19,6,3] 
print(lst9)
for i in range(1, len(lst9)):
    j=i-1
    while j>=0:
        if(lst9[j]>lst9[j+1]):
            lst9[j+1],lst9[j]=lst9[j],lst9[j+1]
        j-=1    
print(lst9)

# lst10=[10,8,5,20,19,6,3] 
# for i in range(len(lst10)):
#   mini=i
#   for j in range(i+1,len(lst10)):
#     if lst10[mini]>lst10[j]:
#       mini=j
#   lst10[i],lst10[mini]= lst10[mini],lst10[i]
#   print(lst10)    

#
a=[10,8,5,20,19,6,3]
for i in range(len(a)-1):
    mini=a.index(min(a[i+1:]))  
    if mini==i:
      a[mini]==a[i]
    else:
      a[i],a[mini]=a[mini],a[i]
    print(a) 
