
myList=[4,2,3,5,1]
myList.sort()
print(myList)

myDic ={1:1,3:3,2:2}
myDic.sort()
print(myDic)

sorted("hello",reverse=True)

sorted([5,3,2,1,4,3])
sorted([[2,1,4],[2,3,4,3],[4,3,4,3]])

sorted({3,2,1})

sorted((3,2,1))

sorted({3:1,2:3,1:4})

myDic ={3:1,2:3,1:4}

sorted(myDic.items(),key=lambda x:x[1],reverse=True)

sorted(['abc','bac','python'],key=lambda x:x[1],reverse=True)