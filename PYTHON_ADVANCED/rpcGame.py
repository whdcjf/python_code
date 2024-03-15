import random
import time
import sys
import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

def rpcComp(user,com):
    if (user + 1) % 3 == com:
        return -1
    elif user == com :
        return 0
    else:
        return 1

rpcValue = {0 : "바위", 1 : "보" , 2 : "가위"}
gameResDic = {-1 : "Lose", 0 : "Draw", 1 : "Win"}

print("[$] 가위/바위/보 게임 Machine [$]")
print("$-+-+-+-+-+-+-+-+-+-+-+-+-$")

userName = input("이름 : > ")
userCoin = 1000

print("[$] {} 님! 대박나세요!".format(userName))
print("[$] 입장을 도와드리겠습니다. 잠시만 기다려주세요...")
time.sleep(3)

while True:
    clearConsole()
    
    print("[User Info]")
    print("-- User Name : {}".format(userName))
    print("-- User Coin : {}".format(userCoin))

    if(userCoin <= 0):
        print("[$] 당신은 파산했습니다.")
        print("[$] 퇴장처리됩니다.")
        sys.exit("[^_^] 또 찾아와주세요! :)")

    print()
    print("[+] Menu")
    print("0", ":" , "Play")
    print("1", ":", "Exit")

    userChoice = input("Choice > ")

    if(userChoice == "1"):
        sys.exit("[^_^] 또 찾아와주세요! :)")
          
    while True:
        print()
        print("이번 게임에 베팅할 코인을 입력해주세요.")
        while True:
            try:
                betCoin = int(input("> "))
            except:
                print("[!] 베팅할 코인 숫자를 입력해주세요.")
                continue
            
            if(betCoin > userCoin):
                print("[!] 가지고 있는 코인보다 많은 코인을 배팅할 수 없습니다.")
            else:
                break

        comChoice = random.randint(0,2)
        print()
        print("[-] 아래 선택지 중 선택해주세요.")
        for key in rpcValue:
            print(key, ":", rpcValue[key])

        print()
        try:
            userChoice = int(input("> "))
        except:
            print("[!] 선택지 0, 1, 2 중에 입력해주세요.")
            continue

        break
    
    print()
    print("[$] 가위!", end="\r")
    time.sleep(1)
    print("[$] 바위!!", end="\r")
    time.sleep(1)
    print("[$] 보!!!!!", end="\r")
    time.sleep(1)
    print("        " * 10)

    print("[$] User : " + rpcValue[userChoice])
    print("[$] Computer : " + rpcValue[comChoice])

    gameRes = rpcComp(userChoice,comChoice)

    print("[$] Game 결과 :", gameResDic[gameRes])
    print()

    if(gameRes == 1):
        userCoin += betCoin
        print("[$] Olleh~~~! 축하합니다! ")
        print("[$] 베팅한 코인을 얻으셨습니다.")
        print("[$] 획득한 코인 : {}".format(betCoin))
    elif(gameRes == -1):
        userCoin -= betCoin
        print("[$] 게임에 지셨습니다. ")
        print("[$] 베팅한 코인이 차감됩니다..")
        print("[$] 차감된 코인 : {}".format(betCoin))
    else:
        print("[$] 게임이 무승부 입니다. ")

    input("[>] 계속하려면 Enter를 누르세요.")