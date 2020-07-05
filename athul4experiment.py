Python 3.7.7 (tags/v3.7.7:d7c567b08f, Mar 10 2020, 10:41:24) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> names=["able","ann","tas"]
>>> "Hi people".join(names)
'ableHi peopleannHi peopletas'
>>> " Gud mrng".join(names)
'able Gud mrngann Gud mrngtas'
>>> " Gud mrng ".join(names)
'able Gud mrng ann Gud mrng tas'
>>> mylist=[1,2,4,5]
>>> mylist=myslist[0:1].append("a")
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    mylist=myslist[0:1].append("a")
NameError: name 'myslist' is not defined
>>> mylist=mylist[0:1].append("a")
>>> mylist
>>> mylist[0:1]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    mylist[0:1]
TypeError: 'NoneType' object is not subscriptable
>>> mylist=[1,2,4,5]
>>> mylist[0:1].append("a")
>>> type(mylist[0:1].append("a"))
<class 'NoneType'>
>>> None
>>> mylist=mylist[0:1].append("a")
>>> type(mylist)
<class 'NoneType'>
>>> mylist[0:1].append("a")
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    mylist[0:1].append("a")
TypeError: 'NoneType' object is not subscriptable
>>> mylist=[1,2,4,5]
>>> mylist[0:1].append("a")
>>> import math
>>> math.sin(10)
-0.5440211108893698
>>> mylist
[1, 2, 4, 5]
>>> mylist.append("a")
>>> mylist
[1, 2, 4, 5, 'a']
>>> mylist[0:1].append("a")+mylist[:]
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    mylist[0:1].append("a")+mylist[:]
TypeError: unsupported operand type(s) for +: 'NoneType' and 'list'
>>> mylist=[1,2,4,5]
>>> my=mylist[0:1]
>>> list1=mylist[1:]
>>> my.append("a")
>>> my
[1, 'a']
>>> my+list1
[1, 'a', 2, 4, 5]
>>> li=my+list1
>>> li
[1, 'a', 2, 4, 5]
>>> li.pop(3)
4
>>> li
[1, 'a', 2, 5]
>>> li.insert(0,4)
>>> li
[4, 1, 'a', 2, 5]
>>> li.append([1,4,6,0[4,5,7]])
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    li.append([1,4,6,0[4,5,7]])
TypeError: 'int' object is not subscriptable
>>> li.append([1,4,6,0[4,5,7]])
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    li.append([1,4,6,0[4,5,7]])
TypeError: 'int' object is not subscriptable
>>> li.append([1,4,6,0,[4,5,7]])
>>> li
[4, 1, 'a', 2, 5, [1, 4, 6, 0, [4, 5, 7]]]
>>> mydict={"a":1,"b":3,"c":[123,12,34]}
>>> mydict["c"]
[123, 12, 34]
>>> mydict["c"][0]
123
>>> mydict["d"]["sexy"]
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    mydict["d"]["sexy"]
KeyError: 'd'
>>> mydict["d"]=["sexy"]
>>> mydict
{'a': 1, 'b': 3, 'c': [123, 12, 34], 'd': ['sexy']}
>>> mydict["e"]="sexy"
>>> mydict
{'a': 1, 'b': 3, 'c': [123, 12, 34], 'd': ['sexy'], 'e': 'sexy'}
>>> mydict.sort(reverse=True)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    mydict.sort(reverse=True)
AttributeError: 'dict' object has no attribute 'sort'
>>> dir(mydict)
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
>>> mydict.popitem(3)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    mydict.popitem(3)
TypeError: popitem() takes no arguments (1 given)
>>> help(mydict.popitem(3))
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    help(mydict.popitem(3))
TypeError: popitem() takes no arguments (1 given)
>>> mydict.popitem()
('e', 'sexy')
>>> mydict
{'a': 1, 'b': 3, 'c': [123, 12, 34], 'd': ['sexy']}
>>> mydict1={'a': 1, 'b': 3,}
>>> lisodic=[mydict,mydict1]
>>> lisodic
[{'a': 1, 'b': 3, 'c': [123, 12, 34], 'd': ['sexy']}, {'a': 1, 'b': 3}]
>>> lisodic[1]
{'a': 1, 'b': 3}
>>> lisodic[1]['a']
1
>>> lisodic[0]['c'][1]
12
>>> list3=[1,2,4]
>>> list4=[2,4,7]
>>> list3-list4
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    list3-list4
TypeError: unsupported operand type(s) for -: 'list' and 'list'
>>> list3[]=input("enter:")
SyntaxError: invalid syntax
>>> list3[]
SyntaxError: invalid syntax
>>> list3[]=0
SyntaxError: invalid syntax
>>> list3[6]
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    list3[6]
IndexError: list index out of range
>>> list3=list(input("enter:"))
enter:5
>>> list3
['5']
>>> list3=input("enter:"))
SyntaxError: invalid syntax
>>> list3=input("enter:")
enter:6
>>> list3
'6'
>>> list3=list(input("enter:"))
enter:5 6 7
>>> list3
['5', ' ', '6', ' ', '7']
>>> list3=list(input("enter:"))
enter:567
>>> list3
['5', '6', '7']
>>> list3=list(input("enter:"))
enter:55,6,77
>>> list3
['5', '5', ',', '6', ',', '7', '7']
>>> list3=list3=list(input("enter:"))
enter:567
>>> list3
['5', '6', '7']
>>> list3=list3=list(input("enter:"))
enter: