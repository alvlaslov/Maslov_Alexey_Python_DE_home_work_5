"""
Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
"""
import os

link = "D:\Study\Code\Python_base\Home work\python.exe"

#var_1
def split_path_files_name_extension(text: str) -> tuple:
    parse_link = text.split(os.sep)
    split_file = parse_link.pop()
    path_to_file = os.sep.join(parse_link)
    print(path_to_file)
    parse_name = split_file.split('.')
    file_extantion = parse_name.pop()
    name_file = '.'.join(parse_name)
    return (path_to_file, name_file, file_extantion)


print(split_path_files_name_extension(link))

#var_2
def file_info(file_path):
    path, filename = os.path.split(file_path)
    name, extension = os.path.splitext(filename)
    return path, name, extension

print(file_info(link))