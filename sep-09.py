'''
POP (Procedure Oriented Programming)
Functions--> A reusable block of code(A block of statements which performs a specific task)

syntax:
def <funcname>(parameters): #func def
        """Doc String"""
        statements(s)...    #body of func
        ....
        return values(s)
fname(args)   #func call
        


def add(a,b):
    c=a+b
    return c
print(add(5,6))
c,d="codegnan","pyhton"
print(add(c,d))
e,f=map(str,input("enter the values").split(','))
print(add(e,f))
print(add[1,2,3],[3,4,2])

Variables length arguments--> *args  We can pass any number of positional
Arguments--> data will be stored in tuple..()


def sample(*a):
    print(a)
    print(type(a))
sample()
sample(2,3,4,5)
sample('codegnan',[2,3],2+5j)

marks=[1,2,3,4,5]
sample(marks)
sample(*marks)

a,*b,c=23,'code','pol',54,25,5
print(a)
print(b)
print(c)

def add(*a):
    print(a)
    result=0
    for i in a:
        if type(i) in [int,float]:
            result=result+i
    return result
print(add(2,3,4,5))
print(add(4,'c','e',3,5,6,1,9))


def batch (name,place,age):
    print(f'{name} is in {place} and age is {age} years')
batch ('codegnan','vizag',21)
batch(name="saketh",age=23)

print(4,5)
print(4,5,sep=':') Here keyword argument is sep and we are changing the default value for sep 

Keyword variables length arguments (**kwargs)--> Any number of keyword  arguments , data is stored in dictionary


'''
def batch(**a):
    print(a)
    print(type(a))
batch()
batch(name="akash",age=21,palce="vizag",branch="cse")
data={'name':["akash","praneeth"],
      'place':["vizag","rajamundry"]}
data.update({"batch":'PFS-VSP-007'})
batch(**data)
          
