from pathlib import Path
import os
def read_file(path):
    file_path = Path(path)
    if file_path.exists() and file_path.is_file():
        with open (file_path, mode="r", encoding="utf-8") as f:
            for row in f:
                print(row.strip())
    elif file_path.exists() == 0:
        raise FileExistsError("Файл отсутсвтует")
    elif os.access(file_path) == 0:
        raise PermissionError("Нет прав доступа для чтения файла")
    else:
        raise OSError("Возникли другие ошибки ОС")
path = input("Введите путь до файла. ")
read_file(path)
