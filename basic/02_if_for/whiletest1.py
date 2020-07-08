prompt='''
---------------------------------
        커피 자판기 메뉴
---------------------------------
     1. 커피 메뉴 입력        
     2. 커피 메뉴 삭제
     3. 커피 메뉴 리스트
     4. 커피 메뉴판
     5. 종료
---------------------------------
    메뉴선택 >>>>'''
menudic = {'coffee':2000} 
while True:
    print(prompt)
    menu=input()
    print(menu)
    if menu =='1':
        print("커피메뉴를 추가합니다")
        name=input("메뉴명>>>")
        price=int(input("가격>>>"))
        menudic[name]=price
        print(menudic)
           
    elif menu =='2':
        print("커피메뉴를 삭제합니다")
        name=input("삭제할 메뉴명>>>")
        del menudic[name]
        print(menudic)
    elif menu =='3':
        print("메뉴를 선택해주세요.")
        choicemenu=input("메뉴명>>>")
        if choicemenu in menudic == True:
            money=int(input("돈을 넣어주세요!"))
            if menudic[choicemenu]>money:
                print("금액이 부족합니다.")
            else:
                print("{} 음료가 나옵니다.".format(choicemenu))
                print("남은 금액{}을 받으세요.".format(money-menudic))
        else:
            print("메뉴가 없습니다.")
    elif menu =='4':
        for k,v in menudic.items():
            print("메뉴명 : %s, 가격 : %d" %(k,v))

    
    
    elif menu =='5':
        print("프로그램 종료")
        break  

 