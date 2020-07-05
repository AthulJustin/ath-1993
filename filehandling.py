#files
#file object = open(file_name [, access_mode][, buffering])
myfile=open("blabla.txt","w")#open a file object in write mode
myfile.closed#check if file is closed or not
myfile.name#shows the current file
print(myfile.write("thebbdg hdjxj kkmxkx \n"))#return the number of charachters awritten in it
myfile.close()#closes file only after closing the changes will be replicated
myfile=open("blabla.txt","r")
print(myfile.read(3))#reads 3 character and moves the index to the 3 character
print(myfile.read())
myfile.close()
myfile=open("blabla.txt","r")
str1=myfile.read(5)
print(str1)
myfile.close()

