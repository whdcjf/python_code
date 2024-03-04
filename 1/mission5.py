print("[+] Simple Shell")

while (True):
    cmd = input("> ")

    if(cmd == "exit"):
        break
    
    if(len(cmd) > 10):
        print("[+] 잘못된 명령어입니다.")
        continue

    print(cmd + "가 실행 되었습니다")

print("shell 을 종료합니다.")