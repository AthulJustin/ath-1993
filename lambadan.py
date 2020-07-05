#lamda positional function
from functools import reduce
add=lambda x,y=10: x+y
print(add(3))
print(add(3,5))
#lambda *args
add= lambda *x: sum(x)
print(add(1,2,3,4))
#lambda *kwargs
add=lambda **x: sum(x.values())
print(add(a=3,b=5,c=7))
#lambda with map
c=[1,2,3,4,5]
cuber=list(map(lambda x: x**3, c))
print(cuber)
#filter and filter in lambda
def checkAge(a):
    if a>18:
        print("Adult")
        return a
a=[1,2,35,90,19]
adults=filter(checkAge, a)
print(list(adults))
adults2=filter(lambda x: x > 18, a)
print(list(adults2))
#reduce function reduce in lambda{round off addition and multiplication}
def summer(a, b):
    return a + b
L = [10, 20, 30, 40]
result = reduce(summer, L)
print(result)
L2 = [10, 20, 30, 40,50]
result2 = reduce(lambda a, b: a + b, L2)
print(result2)
#lambda in dictionary items() result is list of tuples here [('a',2),('b',1)]
mydiction= {"a":2, "b": 13 }

my=list(map(lambda x: x[1]**2, mydiction.items()))#x=('a',2) and x=('b',1) x[0]='a' and x[0]='b',x[1]=2 and x[1]=13 on each iteration
print(my)
# list of functions in lambda
def adder(x):
    return x+x
def multip(x):
    return x*x
listfun=[multip,adder]
ls=[]
for i in range(6):
    sq=list(map(lambda x:x(i), listfun))
    ls.append(sq)
    print(sq)
print(ls)
#reduce function
def summer2(a, b):
    return a * b
Lw = [10, 20, 30, 40]
resultc = reduce(summer2, Lw)
print(resultc)
Lw2 = [10, 20, 30, 40,50]
resultc2 = reduce(lambda a, b: a * b, Lw2)
print(resultc2)

