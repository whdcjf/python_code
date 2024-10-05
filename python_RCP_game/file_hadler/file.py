with open("mission_1.txt", "r") as f:
    dataList = f.read().splitlines()

dataList[3420] = "Data 3421 : segfault{cange it !!!}"

with open("mission_clear.txt", "w") as f:
    for data in dataList:
        f.write(data + "\n")