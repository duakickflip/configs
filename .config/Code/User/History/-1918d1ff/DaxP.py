def read_file_to_array(file_path: str) -> list:
    file_data = []
    with open(file=file_path, mode="r", encoding="UTF-8") as file:
        file_data.append(int(file.readline()))
    return file_data

print(read_file_to_array("1.txt"))