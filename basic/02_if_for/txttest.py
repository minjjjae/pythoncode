# f=open("test.txt",'w')
# f.write("txt파일 생성")
# f.close()

f=open("./basic/02_if_for/test.txt","r")
line="a"
while line:
    line = f.readline()
    print(line)
f.close()