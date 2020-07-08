import sys

# student={'idx':0,'name':'','major':'','adr':'','number':0}

def Enrollment(studentlist):
    student={}
    while True:
        idx=input("학번을 입력하세요 >> ")
        if idx.isdecimal():
            idx=int(idx)
            break
        else:
            print("숫자를 입력해주세요")
    name=input("학생이름을 입력하세요 >> ")
    major=input("전공을 입력하세요 >> ")
    adr=input("주소를 입력하세요 >> ")
    while True:
        number=input("전화번호를 입력해주세여 >> ")
        if number.isdecimal():
            number=int(number)
            break
        else:
            print("숫자를 입력해주세요")

    student['idx']=idx
    student['name']=name
    student['major']=major
    student['adr']=adr
    student['number']=number

    studentlist.append(student)

    print(studentlist)

def Update(studentlist):
    student={}
    print("학생정보를 수정합니다.")
    idx=int(input("수정할 학번을 입력하세요 >> "))
    for i in range(0,len(studentlist)):
        if studentlist[i]['idx']==idx:
            name=input("학생이름을 입력하세요 >> ")
            major=input("전공을 입력하세요 >> ")
            adr=input("주소를 입력하세요 >> ")
            number=int(input("전화번호를 입력해주세여 >> "))

            student['idx'] = idx
            student['name']=name
            student['major']=major
            student['adr']=adr
            student['number']=number

            studentlist[i]=student
            break
    print(studentlist)

def Delete(studentlist):
    idx=int(input("삭제할 학번을 입력하세요 >> "))
    for i in range(0,len(studentlist)):
        if studentlist[i]['idx']==idx:
            del studentlist[i]
            break

def List(studentlist):
    for i in range(0,len(studentlist)):
        print(studentlist[i])

def Quit():
    print("종료합니다.")
    sys.exit()