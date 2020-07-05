# Calling a function as argument
def sumofsqr(a):
    x,b=9,50
    x1,b1=a(x,b)
    s=x1+b1
    return('The square are {0} , {1} and the sum of sqaure is {2} '.format(x1,b1,s))
def sqr(p,q):
    p,q=p**2,q**2
    return(p,q)
p=sumofsqr(sqr)
print(p)
    
