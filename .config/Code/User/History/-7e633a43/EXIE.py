array = []
with open('1.txt', mode='r', encoding='UTF-8') as file:
    for _ in range(11):
        array.append(int(file.readline()))
    
counter = 0
summa = 0
max = float('-inf')
for i in range(2, len(array), 3):
    if array[i] % 7 == 0 or array[i - 1] % 7 == 0 or array[i - 2] % 7 == 0:
        summa = sum(array[i - 2:i + 1])
        if summa > max:
            max = summa

print(counter, max)