def sample(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
def addnum1(*n,a="hi"):
    total=0
    for i in n:
        total+=i
    return total, a
def fncnme1(a,b):
    s=a*b
    return "\\nthe product of the the values are ",s
