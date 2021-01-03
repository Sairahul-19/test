#merging 2 arrays

arr1=[1,2,3,4]
arr2=[5,6,7,8]
arr3=arr1+arr2
print(arr3)

#program to print the following
#Hello
#Hell
#Hel
#He
#H


a=  "Hello"
for i in range(len(a),0,-1):
    print(a[0:i])

#covert into matrix  

arr=[1 ,0, 1, 0, 1,0 ,1 ,0 ,1 ,0,1 ,0 ,1 ,0 ,1,0 ,1 ,0 ,1 ,0,1 ,0 ,1 ,0 ,1]  
for  i in range(5):
    r=[]
    for j in range(5):
        r.append(arr[5*i+j])
    print(r)    
    


r=1
print('in order')
for i in range(0,5):
    k=[]
    for j in range(0,5):
        if r==10:
            r=0
        k.append(r)  
        r+=1
    print(k)    
        
         

