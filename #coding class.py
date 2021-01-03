#coding class
arr1=[1,2,3,4,5,6,7,8,9,10]
arr=[]
for i in range(len(arr1)):
    m=arr1[i]+i
    arr.append(m)
print(arr)  

"""#create an array that can hold 10 values in it. add index value of the element to it and print
n=int(input())
print([int(input())+i for i in range(n)])"""

#accepting a sentence as input and getting output in revers

s = "i love you"
words = s.split(' ')
string =[]#list(words)
string.append(words)
string.reverse()
print("Reversed String:")
print(string)
print(" ".join(string))
print(type("c"))
     


