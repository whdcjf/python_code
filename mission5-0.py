while (True):

    try:
        num = int(input("숫자를 입력해 주세요 > "))

        if ( num >= 100 ):
           break

        if (num == 50):
            print("half")
            continue

        print("다시 입력해 주세요")
        
    except:
        print("숫자를 입력해주세요")

print("탈출완료")