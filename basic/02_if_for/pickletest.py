import pickle

data ={1:'python', 2:'you need'}
print(type(data))

# f=open(test.pickle, 'wb')
# pickle.dump(data, f)
# f.close()

# with open("test.pickle", 'wb') as f:
#     pickle.dump(data, f)

# datab=pickle.dump(data)
# print(type(datab))

with open("test.pickle", 'rb') as f:
    data=pickle.load(f)
    print(data)
    print(type(data))