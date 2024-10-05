import requests

with open('userID.txt', 'r') as f:
    userList = f.read().splitlines()

for user in userList:
    param = {"userID" : user}
    response = requests.post('http://192.168.200.128/python/check.php', data = param)

    if 'Not Possible' in response.text:
        result = "Not Possible"
        print("[{}] request! => {}".format(user, result))

    else:
        result = "Possible"

