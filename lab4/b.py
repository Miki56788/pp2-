import os

def list_files_and_folders(folder_path):
    if os.path.exists(folder_path):
        print(f"Содержимое папки '{folder_path}':")
        for item in os.listdir(folder_path):
            item_path = os.path.join(folder_path, item)
            if os.path.isdir(item_path):
                print(f"Папка: {item}")
            else:
                print(f"Файл: {item}")
    else:
        print("Указанная папка не существует.")


folder_path = "lab4"

list_files_and_folders(folder_path)