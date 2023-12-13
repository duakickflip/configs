array = []
with open('1.txt', mode='r', encoding='UTF-8') as file:
    array.append(file.readline())
    print(array)