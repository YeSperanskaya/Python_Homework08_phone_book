# на Отлично в одного человека надо сделать консольное приложение Телефонный 
# справочник с внешним хранилищем информации, и чтоб был реализован основной 
# функционал - просмотр, сохранение, импорт, поиск, удаление, изменение данных.

# импорт нужной программы

import json



# просмотр
def read_file():
    f = open('phone_book.json', 'r')
    f.read()



# сохранение
def save_file():
    f = open('phone_book.json', 'a') #a открытие на дозапись информация добавляется в конце
    name = input('введите имя: ')
    num = input('введите номер: ')
    phone_book[name] = num
# импорт

# поиск
print("c" in the_dict)

#удаление
del phone_book[name]

# изменение данных
phone_book[name] = num

# создание файла словаря:
phone_book = dict()

with open('phone_book.json', 'w') as file:
    json.dump(phone_book, file)

print(read_file())