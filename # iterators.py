# iterators

"""lst=[1,2,3,4,5]
#iter()
#next()
#_iter_()
#_next_()
it=iter(lst)
print(it)
print(next(it))
#print(next(it))
#print(next(it))
#print(next(it))
#print(next(it))
#print(next(it))
for i in it:
    print(i)"""

class Topten:
    def __init__(self):
        self.num=1
    def __lter__(self):
        return self
    def __next__(self):
        if self.num<=10:

            val=self.num
            self.num+=1
            return val
        else:      
            raise StopIteration
values=Topten()
"""print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))"""
for i in values:
    print(i)  

"""def topten():
    yield 1
    yield 2
values=topten()
print(next(values))
print(next(values))
for i in values:
    print(i)  

def top():
    n=1
    while n<=10:
        sq=n*n
        yield sq
        n+=1
values=top()
for i in values:
    print(i)"""  
