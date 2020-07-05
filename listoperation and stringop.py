#lists and pending string functionalities
#More on strings
l=[1,2,3,4,5]
l2=["a","b","v",2,5,6]
l3=["adfg",234,1.2334,"redemption"]
l4=[1,23,4,["aaa","jjj",8,99],"decs",2]
l5=l+l2+l3+l4
print("\n",l)
print("\n",l2)
print("\n",l3)
print("\n",l4)
print("\n",l5)
print("\n",l[3:5])
print("\n",l3[0][:2])
# special scenarios print("\n",l3[0:2][0:2][0:2])
#l6=[002,003,004]
#print("\n",l6)
#Modifying list remove, insert, append
l2.remove("a")
l2.remove("v")
l2.remove(2)
print(l2)
l2.insert(3,78)
print(l2)
l3.append([2,34.5])
print(l3)
l3.pop()
print(l3)
#l3[0:3].append("mayavi")
#print(l3[0:3])
#Sorting only works on homogenous elements
l.sort(reverse=True)
print(l)
l7=[[1,2,3],[6,1,4],[9,5,4]]
l7.sort()
print(l7)
l7[0].sort(reverse=True)
print(l7)


