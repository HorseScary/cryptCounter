file = open("crypts", "r")
lines = file.readlines()

crypts = []

for i in lines:
    crypts.append([i.split(':')[0], int(i.split(':')[1])])

totalCrypts = 0
while True:
    room = input()

    for i in crypts:
        if i[0].lower() == room.lower():
            totalCrypts += i[1]
            print(totalCrypts)
