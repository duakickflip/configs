array = []
with open(file='file.txt', mode='r', encoding='UTF-8') as file:
    for _ in range(4000):
        array.append(int(file.readline()))
sum=0
max=float('-inf')
counter=0
for i in range(len(array)):
    for j in range(len(array)):
        sum=0
        if (array[i] - array[j]) % 2 == 0 and (array[i] % 31 == 0 or array[j] % 31 == 0):
            counter+=1
            sum=array[i]+array[j]
            if sum>max:
                max=sum

print(counter, max)