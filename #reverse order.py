#reverse order


arr1 = [1, 2, 3, 4, 5];     
      
arr2 = [None] * len(arr1);    
        
for i in range(0, len(arr1)):    
    arr2[i] = arr1[i];     
     
arr2.reverse()  
         
print("Elements of new array: ")  
for i in range(0, len(arr2)):    
   print(arr2[i])

arr3=arr1.reverse()
print(arr3)     