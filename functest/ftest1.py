def add(a,b):
    total=a+b
    print(total)
    return total


print(add(2,3))





c = add1(2,6)
print(c)
print(type(c))


def say():
    return 'hi'

print(say())
c=say()
print(c)


def add2(a,b):
    print("%d,%d의 합은 %d입니다."%(a,b,a+b))
c=add2(3,4)
print(c)

def add1(a,b):
    return a+b


print(3,5,6,6,sep=",",end="\n")