Python 3.7.7 (tags/v3.7.7:d7c567b08f, Mar 10 2020, 10:41:24) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> mytt="12234"
>>> mytt1="3456"
>>> mytt3=list(mytt)+list(mytt1)
>>> mytt3
['1', '2', '2', '3', '4', '3', '4', '5', '6']
>>> mylist=[1,34,2,"the",[1,3,4]]
>>> mylist
[1, 34, 2, 'the', [1, 3, 4]]
>>> mytuple=(1, 34, 2, 'the', [1, 3, 4])
>>> mylist[4]
[1, 3, 4]
>>> mylist[4]=[3,2,4]
>>> mylist
[1, 34, 2, 'the', [3, 2, 4]]
>>> mytuple[4]
[1, 3, 4]
>>> mytuple[4]=[2,4,7]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    mytuple[4]=[2,4,7]
TypeError: 'tuple' object does not support item assignment
>>> mytuple[-1][1]=78
>>> mytuple
(1, 34, 2, 'the', [1, 78, 4])
>>> mytuple[-1][:]=[2,4,7]
>>> mytuple
(1, 34, 2, 'the', [2, 4, 7])
>>> mystr56="sddddcc"
>>> mymystr56.replace("sd","XXX")
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    mymystr56.replace("sd","XXX")
NameError: name 'mymystr56' is not defined
>>> mystr56.replace("sd","XXX")
'XXXdddcc'
>>> mystr56=mystr56.replace("sd","XXX")
>>> mystr56
'XXXdddcc'
>>> mylist.append("aa").index(3)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    mylist.append("aa").index(3)
AttributeError: 'NoneType' object has no attribute 'index'
>>> mylist.index(2)
2
>>> mylist
[1, 34, 2, 'the', [3, 2, 4], 'aa']
>>> mylist.index(2).append("aa")
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    mylist.index(2).append("aa")
AttributeError: 'int' object has no attribute 'append'
>>> mylist[0:3].append("xx")
>>> mylist
[1, 34, 2, 'the', [3, 2, 4], 'aa']
>>> mylist=mylist[0:3].append("xx")
>>> mylist
>>> mylist
>>> mylist=[1, 34, 2, 'the', [3, 2, 4], 'aa']
>>> mylist
[1, 34, 2, 'the', [3, 2, 4], 'aa']
>>> mylist=mylist[0:3].append("xx")
>>> mylist
>>> mylist=[1, 34, 2, 'the', [3, 2, 4], 'aa']
>>> mylist.remove(34)
>>> mylist
[1, 2, 'the', [3, 2, 4], 'aa']
>>> names=["brijesh","athul","aishwar"]
>>> names.sort()
>>> names
['aishwar', 'athul', 'brijesh']
>>> 
==== RESTART: C:/Users/athuljux/AppData/Local/Programs/Python/Python37/x.py ====
Hi athul
Hi baby
Hi red
>>> 
==== RESTART: C:/Users/athuljux/AppData/Local/Programs/Python/Python37/x.py ====
Hi athul
Hi baby
Hi red
>>> 