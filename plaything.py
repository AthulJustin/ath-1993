def dictmanip(d2):
    print(d2)
    for i,j in d2.items():
        print("The key is {0}, the value is {1}".format(i,j))
def dictcreator():
    pp={}
    while True:
        _1=input("Do you want Key to be a number ?Enter your choice Yes/No:")
        if _1=="Yes":
            key = int(input("Enter the key: "))
        else:
            key = input("Enter the key: ")
        _2=input("Do you want Value to be a number ?Enter your choice Yes/No:")
        if _2=="Yes":
            value = int(input("Enter the value: "))
        else:
            value = input("Enter the value: ")
        pp[key]=value
        #Lisofdic.append(pp)
        _3=input("Do you want to continue enter your choice Yes/No :")
        if _3=="No":
            break
    #print(Lisofdic)
    return(pp)
#Lisofdic=[]
dictmanip(dictcreator())

    
