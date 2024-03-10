## 가위, 바위, 보 시스템 만들기 프로젝트

import random
import time

def random_list ():
    while (True):
        com_list = ["주먹", "가위", "보자기"]
        com_RCP = random.choice(com_list)
        return com_RCP

user_coin = 100


## 시스템 처음 말 ----------------------------------------
print("""\
[*] 안녕하세요. 이 프로그램은 가위바위보 프로그램입니다.
    
    게임시작을 하시게 되면 기본 코인 100 코인을 받을 수 있습니다.
    이 코인은 가위, 바위, 보 게임을 할때 필수적으로 걸어야 합니다. 또한,
    컴퓨터와 가위, 바위, 보를 해서 이길시에는 여러분이 건 코인만큼 돌려받을 수 있습니다.
    
    하지만 컴퓨터와의 대결에서 지는 경우에는 여러분이 건 코인을 모두 잃게 됩니다. 
    보유 코인을 전부 잃게 되면 자동적으로 게임은 종료가 됩니다.
    
    수단과 방법을 가리지 말고 컴퓨터를 이겨보세요!
    여러분의 행운을 빌겠습니다!\
""")
## -------------------------------------------------------

## 사용자 이름 받고, 게임 실행 여부 ------------------------
user_name = input("\n[+]사용자 이름을 적어주세요 >> ")
start_fir = input("""\
                  
[+] 안녕하세요 {} 님
                  
[+] 시작을 원하시면 \"y\" 버튼을 눌러보세요!  
    (다른 버튼을 누르시면 게임은 종료됩니다) > \
""".format(user_name))

if (start_fir == "y"):
    print("""     
[+] 게임의 규칙을 설명해 드리겠습니다.
   1. 여러분은 게임을 시작하실때 필수적으로 코인을 걸어야 합니다.
   2. 무엇을 낼지 고민 하시고 입력 하시면 컴퓨터가 3초의 카운트를 시작합니다.
   3. 가위 : 가위, 주먹 : 주먹 , 보자기 : 보자기  낼수 있습니다. (오타없이 입력해주세요)     
""")

while (start_fir == "y"):  

    print("[+] 현재 코인 {}".format(user_coin))

    try:
        betting_coin = int(input("[+] 코인을 걸어주세요 > "))   

        while (betting_coin > user_coin) :
            print("[+] 현재있는 코인보다 많이 걸 수 없습니다. \n")
            print("[+] 현재 코인 {}".format(user_coin))
            betting_coin = int(input("[+] 배팅할 코인을 입력해 주세요 > "))

        while (betting_coin <= 0 ):
            print("0 보다 낮게 입력할 수 없습니다.\n")
            print("[+] 현재 코인 {}".format(user_coin))
            betting_coin = int(input("[+] 배팅할 코인을 입력해 주세요 > "))
    except:
        print("\n[+] 숫자(정수)를 입력해 주세요!\n")
        continue

    user_data = input ("""\
[+] 가위, 주먹, 보자기 중 하나를 입력하시면 카운트가 시작됩니다. > \
""")
    
    if (user_data == "가위" or user_data == "주먹" or user_data == "보자기"):

        while(user_coin > 0):
            for i in range(3,0,-1):
                print(i,"...")
                time.sleep(1)

            com_result = "가위"

            while (user_data == com_result):
                user_data = input("\n컴 : {} VS {}님 : {} 로 비겼습니다! 다시 골라주세요 > ".format(com_result,user_name,user_data))
                for i in range(3,0,-1):
                    print(i,"...")
                    time.sleep(1)

                com_result = random_list()    

            if (user_data == "가위" and com_result == "주먹"):
                print("컴 : {} VS {}님 : {} (으)로 졌습니다.. ".format(com_result,user_name,user_data))
                user_coin = user_coin - betting_coin

                if (user_coin > 0):
                    print("보유코인 : {}".format(user_coin))
                    re_try = input("게임을 더 진행 하시고 싶으시면 \"y\" 키를 눌러주세요. (게임을 종료하고싶으시면 아무키나 눌러주세요) > ")
                    if (re_try == "y"):
                        break
                    else :
                        print("게임을 종료하겠습니다.  보유코인 {}원으로 종료되었습니다.".format(user_coin))
                        exit()

            elif (user_data == "주먹" and com_result == "보자기"):
                print("컴 : {} VS {}님 : {} (으)로 졌습니다.. ".format(com_result,user_name,user_data))
                user_coin = user_coin - betting_coin
                
                if (user_coin > 0):
                    print("보유코인 : {}".format(user_coin))
                    re_try = input("게임을 더 진행 하시고 싶으시면 \"y\" 키를 눌러주세요. (게임을 종료하고싶으시면 아무키나 눌러주세요) > ")
                    if (re_try == "y"):
                        break
                    else :
                        print("게임을 종료하겠습니다.  보유코인 {}원으로 종료되었습니다.".format(user_coin))
                        exit()

            elif (user_data == "보자기" and com_result == "가위"):
                print("컴 : {} VS {}님 : {} (으)로 졌습니다.. ".format(com_result,user_name,user_data))
                user_coin = user_coin - betting_coin

                if (user_coin > 0): 
                    print("보유코인 : {}".format(user_coin))
                    re_try = input("게임을 더 진행 하시고 싶으시면 \"y\" 키를 눌러주세요. (게임을 종료하고싶으시면 아무키나 눌러주세요) > ")
                    if (re_try == "y"):
                        break
                    else :
                        print("게임을 종료하겠습니다.  보유코인 {}원으로 종료되었습니다.".format(user_coin))
                        exit()

            elif (user_data == "가위" and com_result == "보자기") :
                print("컴 : {} VS {}님 : {} 로 이겼습니다. 축하드려요!".format(com_result,user_name,user_data))
                user_coin = user_coin + betting_coin
                print("[+] 현재 코인 {}\n".format(user_coin))
                re_try = input("게임을 더 진행 하시고 싶으시면 \"y\" 키를 눌러주세요. (게임을 종료하고싶으시면 아무키나 눌러주세요) > ")
                
                if (re_try == "y"):
                    break
                else :
                    print("게임을 종료하겠습니다.  보유코인 {}원으로 종료되었습니다.".format(user_coin))
                    exit()
            
            elif (user_data == "주먹" and com_result == "가위") :
                print("컴 : {} VS {}님 : {} 로 이겼습니다. 축하드려요!".format(com_result,user_name,user_data))
                user_coin = user_coin + betting_coin
                print("[+] 현재 코인 {}\n".format(user_coin))
                re_try = input("게임을 더 진행 하시고 싶으시면 \"y\" 키를 눌러주세요. (게임을 종료하고싶으시면 아무키나 눌러주세요) > ")
                
                if (re_try == "y"):
                    break
                else :
                    print("게임을 종료하겠습니다.  보유코인 {}원으로 종료되었습니다.".format(user_coin))
                    exit()

            elif (user_data == "보자기" and com_result == "주먹") :
                print("컴 : {} VS {}님 : {} 로 이겼습니다. 축하드려요!".format(com_result,user_name,user_data))
                user_coin = user_coin + betting_coin
                print("[+] 현재 코인 {}\n".format(user_coin))
                re_try = input("게임을 더 진행 하시고 싶으시면 \"y\" 키를 눌러주세요. (게임을 종료하고싶으시면 아무키나 눌러주세요) > ")
                
                if (re_try == "y"):
                    break
                else :
                    print("게임을 종료하겠습니다.  보유코인 {}원으로 종료되었습니다.".format(user_coin))
                    exit()

            else :
                print("[+] 오류발생. 다시 시작합니다.가위, 주먹, 보자기 셋중에 하나를 입력해 주세요\n")
                break
            break

        if(user_coin <= 0):
            print("코인을 다 잃으셨네요.. 다음에 다시 도전해주세요!")
            break
    else :
        print("\n[+] 가위, 주먹, 보자기 셋중에 하나를 입력해주세요\n")
        continue
if (start_fir != "y"):
    print("[+] 게임을 종료합니다.")
