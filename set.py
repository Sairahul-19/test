s1={"hello","good","morning",'hello'}
l1=[1,2,3,2,5,4,5,2,3,5]
l2=[]
#s2={} -getting data type as dict

s2=set(l1) #convert to set
#s2=l1-it convert into list
print(type(s2))
print(l1)
print(s2)
print('data type is',type(s1))
#print(s1[0])- 'set' object is not subscriptable
for x in s1:
    print(x)

print(s1) 

s1.add('students')
print(s1)
#l2=list(s1)
#print(l2)

s1.update(['pen','pencil','eraser'])
print(s1)

print('after deleting a str')
s1.remove('good')
#s1.remove('rahul') -s1.remove('rahul')
                    #KeyError: 'rahul'
s1.discard('rahul')  #it shown no error                  
print(s1)

s1.pop() #removes last element
print(s1)

s2={1,2,3}
s3=s1.union()
print(s3)

str="Good Morning" 
nstr=str.replace("morning","evening") 
print(nstr) 

print(len(str))
