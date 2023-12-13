array = []
with open('1.txt', mode='r', encoding='UTF-8') as file:
    for _ in range(11):
        array.append(int(file.readline()))
    
for i in range(2, len(array), 3):