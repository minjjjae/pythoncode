str1="abcdefgh"
list1=[1,2,3,4,5,6]
tuple1=(1,2,3,4,5,6)
dic1={1:"첫번째",2:"두번째"}
set1={1,2,3,4}

for i in range(1,10):
    print(i)

for i in range(2,10):
    print("\n--[%d단]--"%i)
    for j in range(1,10):
        print("%d x %d = %2d"%(i,j,i*j))
print()

for x in range(1,10):
    for y in range(2,10):
        print("{} x {} = {:2}".format(y,x,x*y),end='    ')
    print( )

a = [1,2,3,4,5]
result =[num*3 for num in a if num %2==0]
print(result)

result =[]
for num in a:
    if num%2==0:
        result.append(num*3)
print(result)
