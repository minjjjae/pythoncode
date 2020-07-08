import test2

studentlist=[
    {'idx':1,'name':'a','major':'d','adr':'o','number':1},
    {'idx':2,'name':'b','major':'e','adr':'p','number':1},
    {'idx':3,'name':'c','major':'f','adr':'q','number':1},
]

def sys(menu):
        if menu=='1':
            test2.Enrollment(studentlist)
            print(page)
        
        elif menu=='2':
            test2.Update(studentlist)
         
        elif menu=='3':
            test2.Delete(studentlist)

        elif menu=='4':
            test2.List(studentlist)

        elif menu=='5':
             quit()
        


              
while True:
    menu=input('''
    다음 중에서 하실 일을 골라주세요 :
    1. 입력
    2. 수정
    3. 삭제
    4. 목록
    5. 종료
    ''')

    sys(menu)