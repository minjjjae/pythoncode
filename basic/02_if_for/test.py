import time,random ,pickle,json
# print("문제를 풀어보세요")

# count=0
# for i in range(3):
        
#     i1=random.randint(1,50)
#     i2=random.randint(1,50)
#     print(i1,"+",i2,"=")
#     result=int(input())
#     if result==i1+i2:
#         print("정답입니다.")
#         count=count+1
#     else:
#         print("틀렸습니다.")

# print(count)



# print("문제를 풀어보세요")

# for i in range(3):

#     operator=["+","-","*"]
#     i1=random.randint(1,50)
#     i2=random.randint(1,50)
#     op=random.choice(operator)
#     input("엔터를 누르고 20초를 셉니다.")
#     start = time.time()
#     result="%d %s %d" %(i1,op,i2)
#     print(result,"=")
#     c=int(input())
#     if c==eval(result):
#         print("정답입니다.")
#         count=count+1
#     else:
#         print("틀렸습니다.")
# end = time.time()
# print(count)
# print("차이 :",int(abs((end - start)-20)),"초")

print("타자게임을 시작합니다.")
input("게임시작(enter)")
start= time.time()
count=0
words=["나무","구름","파이썬","자바","컴퓨터","선생님","김민재"]
with open('./basic/02_if_for/rank.json','rt')as f:
    rank =json.load(f)

def sortV(x):
    return x[1]
while True:
    print("1.타자게임 2.문제불러오기 3.문제저장하기 4.문제 등록 수정 삭제 5.등수 6.종료하기")
    menu = input("메뉴를 선택하세요\n")
    if menu=='1':
            for i in range(3):
                i1=random.choice(words)
                print(i1)
            
                while True:
                    result=input()
                    if i1==result:
                        print("정답") 
                        count=count+1 
                        break 
                    else:
                        print("다시 하세요")

            end=time.time()
            print(count)
            print('타자시간:{:.0f}초'.format(end-start))
            name=input("사용자 이름을 입력하세요")
            rank[name]=float(end-start)
            print(rank)
        

    elif menu=='2':
        f=open("./basic/02_if_for/word.json","rb")
        json.load(f)
        f.close()
        print(words)
    elif menu=='3':
        f=open("./basic/02_if_for/word.json","wt")
        json.dump(words,f,indent=4)
        f.close()
    elif menu=='4':
        menu1 = input('1.등록 2.수정 3.삭제')
        if menu1=='1':
            print(words)
            quiz=input('문제입력')
            words.append(quiz)
            print(words)
        elif menu1=='2':
            print(words)
            quiz=input('어떤 문제를 수정하나요?')
            index=words.index(quiz)
            quiz=input("수정내용")
            words[index]=quiz
            print(words)
                
        elif menu1=='3':
            print(words)
            quiz=input('문제입력')
            words.remove(quiz)
            print(words)
        else:
            print("메뉴를 잘못 선택하셨습니다.")
    elif menu=='5':
        ranklist=sorted(rank.items(),key=sortV)
        #ranklist=sorted(rank.items(),key=lambda x:x[1])
        num=1
        for k,v in ranklist:
            print("%d등 %s %f" %(num,k,v))
            num=num+1
    
    elif menu=='6':
         break
    else:
        print("메뉴를 잘못 선택하셨습니다.")
with open('./basic/02_if_for/rank.json','wt')as f:
    json.dump(rank,f,indent=4)

    