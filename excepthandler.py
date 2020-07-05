def meth():
    qt=[]
    try:
        while True:
            a=int(input("No1  :"))
            b=int(input("No2  :"))
            print(a/b)
            qt.append(a/b)
            x=input("do you want to continue enter your choice yes/no :")
            if x=="no":
                break
    except ZeroDivisionError:
        print("the divisor cannot be zero go learn basic math!")
    except ValueError:
        print("Enter the proper value, enter a number not a string go learn english")
    except Exception as e:
        print(e)
    else:
        print("Well done! go to your classes")
    return(qt)

