user = {"name":"p2po", "gender":"M", "age" : 25}


print(user["name"] + "님! 안녕하세요~")
print("닉네임을 변경하고 싶으시다고요?")

user["name"] = "crystal"
print("닉네임을 " + user["name"] + " 으로 변경해 드렸어요~\n")

print(user["name"] + " 님의 성별은 " + user["gender"] + " 가 맞으시나요?")

user["gender"] = "W"

print("죄송합니다 착오가 있었군요 " + user["gender"] + " 로 바꿔드렸습니다!\n")

print("취미는 어떻게 되시나요?")

user["habit"] = "운동"
print("취기가 " + user["habit"] + " 이시군요! 저도 " + user["habit"] + " 좋아해요!\n")

print("나이는 ", user["age"], "가 맞으시죠?")
print("아 나이는 비밀이시라구요!? 지워드릴게요 :)\n")

del(user["age"])
print(user)