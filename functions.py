# functions
def f(name):
    print(name*5)

f(5)
f('hi')
f(12.5)

def f1(name,msg='you have a message'):
    print("hello",name,msg)

f1('ali')
f1('revanth','have u r lunch')    
#f1() # f1() missing 1 required positional argument: 'name'

def students(name,*c):
    print('names of',name,'students are')
    for i in c:
        print(i)

students('true','ram','lucky','raj')  
students('ram')

def f2(**gasd):
    for k,v in gasd.items():
        print("%s=%s"%(k,v))

f2(firsr='hello',mid='good',last='morning')  

square=lambda x:x*x
print('square of the given number',square(4))

y=10
z=lambda x:x*y
print(z(5))

