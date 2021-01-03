#class work


a=input("enter the number")


b=0
s=0
  
try:
    n=int(a)
    while n!=0:        
        

        b=n%10
        s+=b
        n=n//10

    print(s)
except:
    try:
        f=float(a)
        print("the type of a is float" )  

    except:
        print("the type of a is",type(a)) 

#program to generate and catch the following expressions
#TypeError
#NameError
#ValueError
#IndexError
#Exception   

# try:
#     '1'+1
# except TypeError:
#     print('TypeError')
# try:
#     int('abc')
# except ValueError:
#     print('ValueError')
# try:
#     hello
# except NameError:
#     print('NameError')
# try:
#     l=[1,2,3]
#     l[3]
# except IndexError:
#     print('IndexError')
       

           

