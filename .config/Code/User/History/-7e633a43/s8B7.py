array = []
with open('1.txt', mode='r', encoding='UTF-8') as file:
    for _ in range(11):
        array.append(int(file.readline()))
    print(array)