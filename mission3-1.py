data = {}

name = input("이름을 말씀해 주세요 : ")

data["name"] = name
print('\n안녕하세요~! 좋은 아침입니다! '+ data["name"] +' 님! \n')

print('저는 과일 좋아하는데')
fruit = input("좋아하는 과일 있으세요? : ")

data["fruit"] = fruit

print('\n아하~ '+ data['fruit'] + '이라는 과일을 좋아하시군요!')
print('제가 바로 ' + data['fruit'] + '준비해 드리겠습니다.')

refruit = input('아 잘못 입력하셨다구요? 다시 입력해주세요~ : ')

data["fruit"] = refruit

print('\n이번에는 '+ data['fruit'] + ' 이라는 과일이 확실하시다구요? 저도 좋아해요 :)')
