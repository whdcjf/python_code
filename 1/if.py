
try :
    score = int(input("점수를 입력해 주세요 >>"))

except:
    print("숫자를 입력해주세요.")
    exit()

if (score == 100) :
    print("100점 축하해요")
elif (score >= 80 and score < 99):
    print("잘했어요")
elif( score >= 40 and score < 79):
    print("노력해요")
else :
    print ("공부하세요") 