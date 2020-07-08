import re

custlist=[{'name':'홍길동','gender':'M','email':'hong1@gmail.com','birthyear':'2000'},
            {'name':'김길동','gender':'M','email':'kim1@gmail.com','birthyear':'2010'},
            {'name':'박길동','gender':'F','email':'park1@gmail.com','birthyear':'1998'},
            {'name':'김철수','gender':'M','email':'kim01@gmail.com','birthyear':'1999'}]
page=3


while True:
    choice=input('''
    다음 중에서 하실 일을 골라주세요 :
    I - 고객 정보 입력
    C - 현재 고객 정보 조회
    P - 이전 고객 정보 조회
    N - 다음 고객 정보 조회
    U - 고객 정보 수정
    D - 고객 정보 삭제
    Q - 프로그램 종료
    ''')  

    if choice=="I":        
        print("고객 정보 입력")
        customer_dic = {'name': '',"gender":'',"email":'',"birthyear":''}
        customer_dic['name']=input("이름을 입력하세요:")

        while True:
            gender = input("성별을 입력하세요(m,M,f,F) >> ")
            if gender == 'm' or gender =='M' or gender == 'f' or gender == 'F':
                gender = gender.upper()
                customer_dic['gender'] = gender
                break
            else :
                print("잘못 입력하셨습니다")
        while True:
            customer_dic['email']=str(input("이메일을 입력하세요:  ")) 
            check=0
            for i in custlist:
                if i['email']==customer_dic['email']:
                    check = 1
            p=re.compile('[a-z][a-z0-9]{4,}@[a-z]{2,}[.][a-z]{2,5}')
            result=p.match(customer_dic['email'])
            if result !=None and check==0:
                break
            elif result==None:
                print('"@"를 포함한 정확한 이메일을 써주세요')
            elif check==1:
                print('중복되는 이메일이 있습니다.')




        while True:
            birthyear = input("출생연도를 입력하세요(4자리숫자) >> ")
            if len(birthyear) == 4 and birthyear.isdecimal():
                customer_dic['birthyear'] = int(birthyear)
                break
            else :

                print("잘못 입력하셨습니다")


        custlist.append(customer_dic)
        page += 1 # page = page + 1

        print(custlist)

    elif choice=="C":
        print("현재 고객 정보 조회")
        if page >=0:
            print("현재 페이지는 {}쪽 입니다." .format(page+1))
            print(custlist[page])
        else:
            print("입력된 정보가 없습니다.")
    elif choice == 'P':
        print("이전 고객 정보 조회")
        if page<=0:
            print('첫 번 째 페이지이므로 이전 페이지 이동이 불가합니다.')
            print(custlist[page])
        else:
            page-=1
            print("현재 페이지는 {}쪽 입니다.".format(page+1))
            print(custlist[page])
    elif choice == 'N':
        print("다음 고객 정보 조회")
        if page>=len(custlist)-1:
            print('마지막 페이지이므로 다음 페이지 이동이 불가합니다.')
            print(custlist[page])
        else:
            page+=1
            print("현재 페이지는 {}쪽 입니다.".format(page+1))
            print(custlist[page])
    elif choice=='D':
        print("고객 정보 삭제")
        
        for i in custlist:
            print(i['name'],':',i['email'],end="")
        print()

        choice1=input('삭제하려는 고객 정보의 이메일을 입력하세요.')
        delok=0
        for i in range(0,len(custlist)):
            if custlist[i]['email']==choice1:
                print('{}고객님의 정보가 삭제되었습니다.'.format(custlist[i]['name']))
                del custlist[i]
                delok =1
            if delok==1:
                break
        
        if delok==0:
            print('등록되지 않은 이메일입니다.')
        print(custlist)
    elif choice=="U": 
        print("고객 정보 수정")
        while True:
            for i in custlist:
                print(i['name'],':',i['email'],end="")
            print()
            idx=-1
            choice1=input('수정하려는 고객 정보의 이메일을 입력하세요.')
            for i in range(0,len(custlist)):
                if custlist[i]['email']==choice1:
                    idx=i
            if idx==-1:
                print('등록되지 않은 이메일입니다.')
                break

            choice2=input('''
            다음 중 수정하실 정보를 골라주세요
            name, gender,birthyear
            (수정할 정보가 없으면 'exit' 입려)
            ''')
            if choice2 in ('name','gender','birthyear'):
                custlist[idx][choice2] =input('수정할 {}을 입력하세요:'.format(choice2))
                break
            elif choice2 =='exit':
                break
            
            else:
                print('존재하지 않은 정보입니다.')
                break

        

                
        
    elif choice=="Q":
        print("프로그램 종료")
        break