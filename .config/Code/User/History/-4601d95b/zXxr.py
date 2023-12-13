array = []

with open(file='file.txt', mode='r', encoding='UTF-8') as file:
    for _ in range(4000):
        array.append(int(file.readline()))


