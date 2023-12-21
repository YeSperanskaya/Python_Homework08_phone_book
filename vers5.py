# Телефонный справочник

import json
# Блок работы с файлами
# функция загрузки из файла информации
def read_file():
    with open('phonebook.json', 'r') as f:
        data = f.read()
        book = eval(data)
        return(book)

# функция переписывает содержимое файла
def write_file(dict):
    with open('phonebook.json', 'w') as f:
        f.write(json.dumps(dict))

# Блок работы со словарем
# Ищем существующий контакт
def find_contact(name):
    data = read_file()
    if len(data) == 0:
        print("В телефонной книге нет контактов")
    else:
        if name in data:
            value = data[name]
            print(f'У абонента {name} номер телефона {value}')
        else:
            print(f'Контакт {name} в телефонном справочнике отсутствует')

def find():
    contact = input('Введите имя контакта: ')
    find_contact(contact)



print(read_file())
data = {}
write_file(data)
print(read_file())
find()