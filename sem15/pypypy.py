import os
import logging
from collections import namedtuple
from pathlib import Path

def gather_directory_info(directory_path):
    log_path = Path('directory_info.log')
    logging.basicConfig(filename=log_path, level=logging.INFO)
    FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_directory'])

    if not os.path.isdir(directory_path):
        logging.error("Указанный путь не является директорией")
        return

    file_info_list = []
    for item in os.listdir(directory_path):
        item_path = Path(directory_path) / item
        name, extension = os.path.splitext(item)
        is_directory = item_path.is_dir()
        parent_directory = Path(directory_path).name
        file_info = FileInfo(name, extension, is_directory, parent_directory)
        file_info_list.append(file_info)
        logging.info(
            f"Файл: {item_path}, Расширение: {extension}, Флаг каталога: {is_directory}, Родительский каталог: {parent_directory}")

    output_path = Path('directory_info.txt')
    with open(output_path, 'w') as file:
        for file_info in file_info_list:
            file.write(
                f"Имя файла: {file_info.name}, Расширение: {file_info.extension}, Флаг каталога: {file_info.is_directory}, Родительский каталог: {file_info.parent_directory}\n")

if __name__ == "__main__":
    import sys

    gather_directory_info(r'C:\Users\Enots\PycharmProjects\dzsem15_aOl\sem15')
