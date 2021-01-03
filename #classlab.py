#classlab
#write a program to accept a sentence and toggle its case

string=input("eneter the str")
str1=string.swapcase()

print("the string in toggle",str1)


#another form
string = input("Please Enter your Own String : ")

string1 = ' '

for i in string:
    if(i >= 'a' and i <= 'z'): 
        string1 = string1 + chr((ord(i) - 32)) 
    elif(i >= 'A' and i <= 'Z'):
        string1 = string1 + chr((ord(i) + 32))
    else:
        string1 = string1 + i
print("The Given String After Toggling Case =  ", string1)
s="a"
sa="A"
print(ord(sa))


#program to print the pairs from a given array whose difference is based on a given key
#sample test case:
#input:
#[1,2,3,4,5,1,4,7,8,9]
#key=2
#output:
#(1,3)(2,4)(3,5)(5,7)(7,9)


lst1 = [int(item) for item in input("Enter the list items : ").split()]
arr1=sorted(lst1)
arr2=list(dict.fromkeys(arr1))
print(arr1)
print(arr2)
key=int(input())
for i in range(len(arr2)):
    if arr2[i]+key in arr2: 
      print('(',arr2[i],',', arr2[i]+key,')  ',end='') 
