# 업 다운게임 프로그램 

import random as r

com_num = r.randrange(1,101)
user_coin = 100

# 업 다운 함수
def updown_game(com_num, user_num):
    if (com_num > user_num):
        print("Up 입니다. \n")
    elif (com_num < user_num):
        print("Down 입니다. \n")
    else :
        return True
    

print("[+] UpDown 게임에 오신걸 환영합니다 !")
print("[+] 기회는 총 '10'번 입니다! \n")

## ----------------- 코인 확인 
while (user_coin > 0):
    life = 10
    print("\n현재 보유한 코인 : {}".format(user_coin))
## ----------------------------------------------------------------
    
## ------------- 코인 제대로 확인 (문자열 입력시 날리기) --------------------
    try:
        betting_coin = int(input("[+] 배팅할 코인을 입력해 주세요 > "))

        while (betting_coin > user_coin) :
            print("[+] 현재있는 코인보다 많이 걸 수 없습니다. \n")
            betting_coin = int(input("[+] 배팅할 코인을 입력해 주세요 > "))

        while (betting_coin <= 0 ):
            print("0 보다 낮게 입력할 수 없습니다.\n")
            betting_coin = int(input("[+] 배팅할 코인을 입력해 주세요 > "))
    except:
        print("숫자를 입력해 주세요\n")
        continue
## -------------------------------------------------------------------------

## ----------------------업다운 게임 실행 -----------------------------
    try:
        while(life > 0):
            print("\n현재 {}번 남았습니다.".format(life))
            user_num = int(input("[+] 숫자를 입력해 주세요 > "))

            result = updown_game(com_num, user_num)
        
            if(result):
                print("정답입니다!\n")
                break

            life = life -1
    except:
        print("숫자를 입력해 주세요")
        life = life -1
        continue
## -------------------------재도전-------------------------------------
    if (life > 0 ):
        user_coin = user_coin + user_coin
        gg = input("게임을 종료하시겠습니까?(Y)  \n(그렇지않으면 아무를 눌러주세요) > ")
        if(gg == "Y" or gg == "y"):
            print("게임이 종료되었습니다.")
            print("총 딴 코인 : {}".format(user_coin))
            exit()
        else :
            continue
    else : 
        user_coin = user_coin - user_coin    
    


    com_num = r.randrange(1,101)

        
print("[+] 코인을 다 잃었습니다.")

## 문제점 : 
## 1. 43번째 줄에서 문자를 입력하게 되면 위로 올라가는것
## 2. 43번째 줄에서 게임 실행할때 횟수가 1이어도 문자를 입력하게 되면 다시 위로 올라가서 기회가 10으로 추가 됨
## 미래의 나 고쳐줘~