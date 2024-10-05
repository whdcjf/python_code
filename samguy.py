import random 

menu = ["돈까스","초밥","짜장면","삼계탕","설빙"]

rand = random.choice(menu)

if rand == "삼계탕" :
    rand = "돈까스"

print("오늘의 점심 메뉴는 : {} 입니다.".format(rand))