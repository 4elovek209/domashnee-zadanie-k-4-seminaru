from pathlib import Path
c = 0
directory = Path(input("Введите путь до вашей папки "))
ext = input("Введите расширение файла ")
for file_path in directory.rglob('*'):
    if file_path.is_file() and file_path.suffix == ext:
        file_path.stat
        print(file_path, file_path.stat().st_size)
else:
    print("Ничего не найдено")
