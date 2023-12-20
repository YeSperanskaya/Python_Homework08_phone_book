# блок работы с файлом
import json

file_phone_book = 'phonebook.json'
phone_book = {}
# при чтении может выдать ошибку соответственно:

# блок команд связанный с чтением
def read_file():
    try:
        data = open(file_phone_book, 'r') #тут берется режим с чтением
        for line in data:
            print(line)
        data.close()
    except FileNotFoundError:
        print(phone_book)

# проверка чтения файла
read_file()



# блок команд связанный с Добавлением нового контакта
# функция работы с файлом
def add_in_file():
    with open(file_phone_book, 'a') as f: # тут все равно добавляется элемент поэтому перезапись не нужна
        json.dump(phone_book, f)

# функция Добавление элемента в словарь
def add():
    name = input('Введите имя: ')
    phone = input('Введите номер телефона: ')
    phone_book[name] = phone
    print(f'Вами было введено имя: {name}, телефон: {phone}')
    add_in_file()

# тестовые команды
add()
read_file()


# Блок команд на удаление контакта
# Удаления работы с файлом
def del_in_file():
    with open(file_phone_book, 'w+') as f: # тут все равно удаляется элемент поэтому перезапись не нужна
        json.dump(phone_book, f)

# Удаление из словаря
def delete_contact():
    name = input('Введите имя контакта, подлежащего удалению: ')
    if (phone_book[name] == name):
        del phone_book[name]
        del_in_file()





# проверка удаления
delete_contact()
read_file()



# Удаление всего содержимого словаря
# команда clear()

# команды для тг-бота 


# изменение

# 23456789
# the_dict = {"a": 1, "b": 2}
 
# if not the_dict.get("A", None):
#     print("Такой ключ не найден")
# Такой ключ не найден
 
# a = the_dict.get("a", None)
# print(a)
# 1

