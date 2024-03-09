import os

folder_path = "lab4"

# Проверяем, существует ли папка "Lab4"
if os.path.exists(folder_path):
    print(f"Содержимое папки {folder_path}:")
    # Получаем список всех файлов и папок внутри "Lab4"
    contents = os.listdir(folder_path)
    for item in contents:
        print(item)
else:
    print(f"Папка {folder_path} не существует.")