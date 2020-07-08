studentlist=[
    {'idx':1,'name':'a','major':'d','adr':'o','number':1},
    {'idx':2,'name':'b','major':'e','adr':'p','number':1},
    {'idx':3,'name':'c','major':'f','adr':'q','number':1},
]


student={'idx':0,'name':'','major':'','adr':'','number':0}

while True:
    menu=input('''
    1. 입력
    2. 수정
    3. 삭제
    4. 목록
    5. 종료
    ''')

    if menu=='1':
        while True:
            idx=input("학번을 입력하세요 >> ")
            if idx.isdecimal():
                idx=int(idx)
                break
            else:
                print("숫자를 입력해주세요")
        name=input("학생이름을 입력하세요 >> ")
        major=input("전공을 입력하세요")
        adr=input("주소를 입력하세요")
        while True:
            number=input("전화번호를 입력해주세여")
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

    elif menu=='2':
        print("학생정보를 수정합니다.")
        idx=int(input("수정할 학번을 입력하세요"))
        for i in range(0,len(studentlist)):
            if studentlist[i]['idx']==idx:
                name=input("학생이름을 입력하세요 >> ")
                major=input("전공을 입력하세요")
                adrr=input("주소를 입력하세요")
                number=int(input("전화번호를 입력해주세요"))

                student['name']=name
                student['major']=major
                student['adr']=adr
                student['number']=number

                studentlist[i]=student
                break
        print(studentlist)

    elif menu=='3':
        idx=int(input("삭제할 학번을 입력하세요"))
        for i in range(0,len(studentlist)):
            if studentlist[i]['idx']==idx:
                del studentlist[i]
                break


    elif menu=='4':
        for i in range(0,len(studentlist)):
            print(studentlist[i])

    elif menu=='5':
        print("종료합니다.")
        break