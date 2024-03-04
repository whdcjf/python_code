data = []

name = input("이름을 말씀해 주세요 : ")
data.append(name)

print('안녕하세요~! 좋은 아침입니다! '+ data[0] +'님! ')
print('저는 과일 좋아하는데')
fru = input("좋아하는 과일 있으세요? : ")
data.append(fru)

data[1] = "바나나" # 받은 내용말고 인위적으로 바꾸기

print('아하~ '+ data[1] + '이라는 과일을 좋아하시군요!')
print('제가 바로 ' + data[1] + '준비해 드리겠습니다.')


# list.append('qksksk')
# list.remove('qksksk')
