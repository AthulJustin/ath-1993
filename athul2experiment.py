Python 3.7.7 (tags/v3.7.7:d7c567b08f, Mar 10 2020, 10:41:24) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("happy")
happy
>>> myth="123abdc"
>>> len(myth)
7
>>> myth=1234
>>> myth.split("a")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    myth.split("a")
AttributeError: 'int' object has no attribute 'split'
>>> mmyth="123abdc"
>>> mmyth.split("a")
['123', 'bdc']
>>> len(mmyth.split("a"))
2
>>> myth2="aaasdtr"
>>> mmyth+myth2
'123abdcaaasdtr'
>>> gmail=ath@gmail.com
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    gmail=ath@gmail.com
NameError: name 'ath' is not defined
>>> gmail="ath@gmail.com"
>>> gmail.split("@" & ".")
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    gmail.split("@" & ".")
TypeError: unsupported operand type(s) for &: 'str' and 'str'
>>> gmail.split("@" && ".")
SyntaxError: invalid syntax
>>> gmail.split("@"&&".")
SyntaxError: invalid syntax
>>> gmail.split("@")
['ath', 'gmail.com']
>>> gmail.split("@")+gmail.split(".")
['ath', 'gmail.com', 'ath@gmail', 'com']
>>> st123="1234556"
>>> list(st123)
['1', '2', '3', '4', '5', '5', '6']
>>> st123=list(st123)
>>> str123
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    str123
NameError: name 'str123' is not defined
>>> l=list(st123)
>>> l
['1', '2', '3', '4', '5', '5', '6']
>>> ":".join(l)
'1:2:3:4:5:5:6'
>>> mystring="fghsxxj"
>>> mystring[:-1]
'fghsxx'
>>> mystring[1:-1]
'ghsxx'
>>> mystring[:]
'fghsxxj'
>>> mystring[::-1]
'jxxshgf'
>>> mystring[::-1]+mystring[:]
'jxxshgffghsxxj'
>>> ooo=12344
>>> list(ooo)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    list(ooo)
TypeError: 'int' object is not iterable
>>> 10/3
3.3333333333333335
>>> ooo="1234"
>>> list(ooo)
['1', '2', '3', '4']
>>> help(list())
Help on list object:

class list(object)
 |  list(iterable=(), /)
 |  
 |  Built-in mutable sequence.
 |  
 |  If no argument is given, the constructor creates a new empty list.
 |  The argument must be an iterable if specified.
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __iadd__(self, value, /)
 |      Implement self+=value.
 |  
 |  __imul__(self, value, /)
 |      Implement self*=value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __reversed__(self, /)
 |      Return a reverse iterator over the list.
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |  
 |  __sizeof__(self, /)
 |      Return the size of the list in memory, in bytes.
 |  
 |  append(self, object, /)
 |      Append object to the end of the list.
 |  
 |  clear(self, /)
 |      Remove all items from list.
 |  
 |  copy(self, /)
 |      Return a shallow copy of the list.
 |  
 |  count(self, value, /)
 |      Return number of occurrences of value.
 |  
 |  extend(self, iterable, /)
 |      Extend list by appending elements from the iterable.
 |  
 |  index(self, value, start=0, stop=9223372036854775807, /)
 |      Return first index of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  insert(self, index, object, /)
 |      Insert object before index.
 |  
 |  pop(self, index=-1, /)
 |      Remove and return item at index (default last).
 |      
 |      Raises IndexError if list is empty or index is out of range.
 |  
 |  remove(self, value, /)
 |      Remove first occurrence of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  reverse(self, /)
 |      Reverse *IN PLACE*.
 |  
 |  sort(self, /, *, key=None, reverse=False)
 |      Stable sort *IN PLACE*.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None

>>> hhhjx=1123
>>> 