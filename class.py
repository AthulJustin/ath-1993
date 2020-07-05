# function/variable that do not start with underscore is public ,one underscore is protected , two underscore private
class ABC():
    t="York"
    def __init__(self,l):
        self.l=l
        self.prod=list(map(lambda x: x*x, self.l))#
    def abc(self):
        print("The Blue Moon")
    def add(self,a,b):
        return a+b
l=[2,3,45,6]
T=ABC(l)
print(T.t)
T.abc()
print(T.add(3,2))
print(T.prod)

