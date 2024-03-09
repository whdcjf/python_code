## 성적관리 프로그램 // for문 

print("[+] 학생 성적 멘토 프로그램")


try :
    score = int(input("성적을 입력해 주세요 > "))

    if (score == 100):
        print( "당신의 점수는 " , score ," 점 이군요~ 대단하시네요~")
    elif (100 > score >= 80 ):
        print("당신의 점수는 " , score ," 점 이군요~ 괜찮아요~")
    elif (79 >= score >= 40):
        print("당신의 점수는 " , score ," 점 이군요~ 노력하세요")
    elif (39 >= score >= 0 ):
        print("당신의 점수는 " , score ," 점 이군요~ 공부 좀 하세요")
    else :
        print("점수를 제대로 입력해 주세요")

except :
    print("숫자를 입력해주세요!")


