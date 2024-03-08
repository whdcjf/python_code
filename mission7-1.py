# 업 다운게임 프로그램 

print("[+] UpDown 게임에 오신걸 환영합니다 !")
print("[+] 기회는 총 '5'번 입니다! \n")

com_num = 99
life = 5

def updown_game(com_num, user_num):
    if (com_num > user_num):
        print("Up 입니다. \n")
    elif (com_num < user_num):
        print("Down 입니다. \n")
    else :
        return True



while (life > 0):

    print("현재 {}번 남았습니다.".format(life))
    user_num = int(input("[+] 숫자를 입력해 주세요 > "))

    result = updown_game(com_num, user_num)

    if(result):
        print("정답입니다!")
        break 

    life = life -1

print("[+] 게임이 종료 됩니다.")