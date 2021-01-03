# list of elements

l1=[1,2,3,4,5]
l2=[1,2,3,"hi",'r',4,5]

l3=[20,10,30,40,50,30,20,30,30]
m=l3[0]
for i in l3:
    if m>i:
        m=i
print('the minimum is',m)
print('the minimum is',min(l1))
print('the maximum is',max(l3))
print('the sum is',sum(l3))
print('the count of 30',l3.count(30))
#l3.sort()
l4=sorted(l3)
print('the sorted list',l3)
print('the sorted list',l4)

if 4 in l1:
    print('found')
else:
    print('not found')

#del(l1)
#print(l1)  
 
L5=[4,8,9,6,41,2,3]
print(L5.remove(2)) 
print(L5) 

L6=[4,8,9,6,41,2,3]
print(L6.pop(2))
print(L6)

var='b' 
print(type(var)) 

g1=[1,2,3,4,5]
for pos, i in enumerate(g1):
    print('the',pos,'of',i)

s=[1,2,3,3,4,5,2,6,3,1]
s1=set(s)
s2=list(s1)
print(s2)

s1=[1,2,3,3,4,5,2,6,3,1]
s1=list(dict.fromkeys(s1))
print(s1)


   
