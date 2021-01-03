#tuples
l=[1,2,3,4]
s={1,2,3}
d={1:"blue",2:"red"}
t=(1,2,3,4,5)
print(type(t),type(l),type(s),type(d))
t=()
t=tuple()
t1=(1)
print(type(t1))
t2=(1,)
print(type(t2))
t3=tuple(l)
print(type(t3),t3)
t4=tuple([1,5,6,7])
t5=(1,2,3,[4,5,6],"hi")
print(type(t5),t5)
t6=1,2,3,"hi"
print(type(t6),t6)
#t6[0]=1   #'tuple' object does not support item assignment
for i in t4:
    print(i)
#t4.add(7)   #'tuple' object has no attribute 'add'
#print(t4.pop(6))   #object has no attribute 'pop'

#del t4
print(t3[1:])
print(t3[:-1])
print(t3[::-1])

t7=(t3+t4)
print(t7)

t8=(t3,t4)
print(t8)

t9=(1,2,3,(5,6))
print(t9)
t10=(10,)*10
print(t10)
st=("hello")*5
print(st)
print(min(t4))

l1=[33,44,55,66]
print(tuple(l1))

if t4==t3:
    print("same")
else:
    print("not same") 

