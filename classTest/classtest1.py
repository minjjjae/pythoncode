# class Cookie:
#     pass

# a = Cookie()

# print(type(a))

class FouraCal:
    mode =1
    def __init__(self,first=1,second=4):
        self.first=first
        self.second=second
        print("생성자")

    def setdata(self,first,second):
        self.first=first
        self.second=second

    def add(self):
        result = self.first + self.second
        return result

a=FouraCal(2)
b=FouraCal(4,7)
c=FouraCal()

print(FouraCal.mode)
print(a.mode)
print(b.mode)
print(c.mode)
print(id(FouraCal.mode))
print(id(a.mode))
print(id(b.mode))
print(id(c.mode))

FouraCal.mode=11
print(FouraCal.mode)
print(a.mode)
print(b.mode)
print(c.mode)
print(id(FouraCal.mode))
print(id(a.mode))
print(id(b.mode))
print(id(c.mode))

print()

a.mode=10
print(FouraCal.mode)
print(a.mode)
print(b.mode)
print(c.mode)
print(id(FouraCal.mode))
print(id(a.mode))
print(id(b.mode))
print(id(c.mode))


a.setdata(3,6)
b.setdata(3,6)


b.first=7
result=a.add()

print(result)
print(id(a.first))
print(id(b.first))


