#The Concept of the Program is to create a list f dictionary by user input
#Dictionary creatot function dictcreator()

def dictcreator():
    pp={}
   
    _1=input("Do you want Key to be a number ?Enter your choice Yes/No:")
    if _1=="Yes":
        key = int(input("Enter the Key: "))
    else:
        key = input("Enter the key: ")
    _2=input("Do you want Value to be a number ?Enter your choice Yes/No:")
    if _2=="Yes":
        value = int(input("Enter the value: "))
    else:
        value = input("Enter the value: ")
    pp[key]=value
    return(pp)
def listdic():
    Listofdic=[]
    i=1
    _4=int(input("Enter Limit :"))
    while i<=_4:
        d2=dictcreator()
        Listofdic.append(d2)
        i+=1
    return(Listofdic)
X=listdic()
print(X)
