import json

data = {"name" : "p2po", "coin": 2000}

#################### 딕셔너리 데이터 제이슨으로 바꾸기 ##########################
json_data = json.dumps(data)

with open("user.txt","r") as f:
    ddat = f.read()

#################### 제이슨 데이터 딕셔너리로 바꾸기 #############################
dicdata = json.loads(ddat)

print(dicdata["name"])