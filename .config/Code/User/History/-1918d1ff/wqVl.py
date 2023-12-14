def read_file_to_array(file_path: str) -> list:
    with open(file=file_path, mode="r", encoding="UTF-8") as file:
        file_data = [map(int, row.strip() for row in file)]
    return file_data

print(read_file_to_array("1.txt"))