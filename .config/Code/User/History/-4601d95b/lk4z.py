array = []

with open(file='file.txt', mode='r', encoding='UTF-8') as file:
    for _ in range(4000):
        array.append(int(file.readline()))


counter = 0
sum = 0
max = float('-inf')
for i in range(len(arrray)):
    for j in range(len(array)):
        if i == j:
            continue
        if array[i] - array[j] % 2 == 0 and (array[i] % 19 == 0 or array[j] % 19 == 0):
            counter += 1
            sum = array[i] + array[j]
            if sum>max:
                max=sum

print(counter, sum)
