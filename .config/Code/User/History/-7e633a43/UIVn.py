array = []
with open(file='file.txt', mode='r', encoding='UTF-8') as file:
    for _ in range(4000):
        array.append(int(file.readline()))
print(array)

for i in range(len(array)):
    for j in range(len(array)):
        if i == j:
            continue
    