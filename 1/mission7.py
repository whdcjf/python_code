import random as ran

com_num = ran.randrange(1,101)
user_coin = 100

def upDawn_game (com_num, user_num):
    if (user_num > com_num):
        print("[*] '{}' 보다 밑 입니다.".format(user_num))
    elif (user_num < com_num):
        print("[*] '{}' 보다 위 입니다.".format(user_num))
    else :
        return True

while(user_coin > 0):
    print("[*] 당신이 가지고 있는 코인 : {}$".format(user_coin))

    bet_coin = int(input("[*] 배팅 할 금액을 적어주세요 >> "))

    while(bet_coin > user_coin):
        print("[*] 당신이 가지고 있는 금액보다 큰 금액을 입력하셨습니다.")
        print("[*]다시입력해 주세요!(당신의 현재 금액은 {}$ 입니다.)".format(user_coin))
        print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
        bet_coin = int(input("배팅 할 금액을 적어주세요 >> "))
        
    life = 10
    while(life > 0):
        print("[*] 남은기회는 {}번 입니다".format(life))
        
        user_num = int(input("[*] 숫자를 입력해 주세요 >> "))
        print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
        gameRes = upDawn_game(com_num, user_num)

        if(gameRes):
            print("[*] 정답입니다!")
            break
            
        life = life - 1

    if(life > 0):
        #게임 승리
        user_coin = user_coin + bet_coin
    else:
        #게임 패배
        user_coin = user_coin - bet_coin

print("코인을 전부 잃었습니다.")
