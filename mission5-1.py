## 쉘 스크립트 프로그램 // while

try:
    print("[+] 명령어를 입력 받습니다\n")

    while (True):

        command = input("> ")

        if (len(command) >= 10):
            print("[+] 명령어가 잘못 됐습니다.\n")
            continue
        
        if (command == "exit" ):
            print("[-] " + command + " 명령어를 실행했습니다. \n")
            print("[+] 프로그램을 종료합니다.")
            break

        print("[-] " + command + " 명령어를 실행했습니다. \n")
except:
    print("제대로 된 입력을 해주세요, 프로그램이 종료됩니다.")

    
