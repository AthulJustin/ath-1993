def sample(first, last, **user_info):
    profile = {}
    print(user_info)
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
def gold(*uppy,don):
    print(don)
    for i in uppy:
        print("\n",i)
_=input("Enter first name")
_1=input("Enter second name")
_2=input("Age")
_3=input("Salary")
_4=input("Job")
print(sample(_,_1,Age=_2,Salary=_3,Job=_4))
gold(_1,_2,_3,_4,don=_)
