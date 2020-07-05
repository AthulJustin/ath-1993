#Functions
#positional arg by the order
def fncnme(a,b):
    print(a+b)
    s=a+b
    return s
apple=fncnme(4,5)
print(apple)
print("\n---------------------------")
#1
def fncnme1(a,b):
    s=a*b
    return "\\nthe product of the the values are ",s
x,y=4,5
apple2=fncnme1(x,y)
print(apple2)
#Keyword argument
def fncnme2(a,b):
    s=b/a
    return "\\nthe quotient tis  of the the values are ",s
apple3=fncnme2(a=20,b=30)
apple4=fncnme2(b=20,a=5)
print(apple3)
print(apple4)
#Dictionary return
def dictret(st,nd):
    p={1:st,2:nd}
    return p[2][2]
print(dictret("bull",[1,2,3,4]))
#string
def city_country(city, country):
    return "{0}, {1}".format(city, country)
print(city_country("Mumbai","India"))
#Looping inside function
def greet(u):
    for i in u:
        m="Hi"+i.title()+"!"
        print(m)
x=["krishna","harry","chowkar"]
greet(x)
#the function will return none if no return is used
print(greet(x))
#dictionary
def dictmanip(d2):
    for i,j in d2.items():
        print("The key is {0}, the value is {1}".format(i,j))
pp={1:"haibach",2:"redstone","age":30}
dictmanip(pp)
#addition using passing argumnts
def addnum(*n,a):
    total=0
    for i in n:
        total+=i
    return total, a
print(addnum(2,5,7,8,9, a="hello"))
#default arguments
#nondefault args should not follow arb pos argument wrong {def addnum(a="hu",b):....}
def addnum1(*n,a="hi"):
    total=0
    for i in n:
        total+=i
    return total, a
print(addnum1(2,5,7,8,9, a="hello"))
print(addnum1(2,5,7,8,9))
#positional args  follow arb pos arg can cause ambiquity {def addnum(b,*num):....}
#arb pos arguments are tuples basically
#Arb keyword arg basically dictionary
def karb(st,nd,**kwr):
    return(st, nd, kwr)
print(karb("theon","greyjoy",age=30,nickname="reek"))
#keyword arg
def sample(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
#print(sample("Athul","justin",age=27,salary=200000,eid="u5566"))

