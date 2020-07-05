i=True
rows, cols = (10, 4)
Datelist = []
count=0
while i==True:
    name=input("Enter name:")
    DOB=input("Enter name:")
    MOB=input("Enter name:")
    YOB=input("Enter name:")
    for rows in Datelist:
        rows.insert(count, [name, DOB, YOB])
    i=input("Do you want to continue True/False:")
    if i == True:
        count = count+1

print(Datelist)
