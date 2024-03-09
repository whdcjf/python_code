# 업 다운게임 프로그램 

print("[+] UpDown 게임에 오신걸 환영합니다 !")
print("[+] 기회는 총 '5'번 입니다! ")
com_num = 80

count = 1

while (count ):

    user_num = int((input("숫자를 입력해주세요! > ")))

    if (count == 5):
        print("기회를 다 사용하셨습니다.. 다음기회에~")
        print("[+] 프로그램이 종료됩니다.")
        break

    elif (com_num == user_num):
        print("정답입니다! 프로그램을 종료합니다")
        print("[+] 프로그램이 종료됩니다.")
        break

    elif (com_num < user_num):
        print("다운 입니다.")
        print("기회 {} 번 사용 : {} 번 남았습니다.".format(count, 5 - count))
        count = count +1
        continue

    elif (com_num > user_num):
        print("업 입니다.")
        print("기회 {} 번 사용 : {} 번 남았습니다.".format(count, 5 - count))
        count = count +1
        continue
    


