def read_file_to_array(file_path: str) -> list:
    with open(file=file_path, mode="r", encoding="UTF-8") as file:
        file_data = list(map(int, [row.strip() for row in file]))
    return file_data


if __name__ == "__main__":
    data = read_file_to_array("files/34.txt")
    counter = 0
    max = float("-inf")
    avg = sum([num for num in data if num % 2 == 0]) / len([num for num in data if num % 2 == 0])

    for i in range(len(data) - 1):
        if (data[i] % min == 0) or (data[i + 1] % min == 0):
            counter += 1
            if data[i] + data[i + 1]> max:
                max = data[i] + data[i]

    print(counter, max)
            
