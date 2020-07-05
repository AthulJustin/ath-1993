#Lambda function is a nameless func since function is object it can treated like an object
lamb=lambda n,y: n+y
print(lamb(10,5))
#map suppose a list and operation need to applied on each element of it
#map func requires two values one the operation to be done and two the variable where the operation is to be done
items=[1,2,3,5,6]
sqrd=list(map(lambda x: x**2, items))
print(items)
print(sqrd)
