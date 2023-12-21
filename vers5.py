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
def find_contact():
    name = input('Введите имя контакта: ')
    data = read_file()
    if len(data) == 0:
        print("В телефонной книге нет контактов")
    else:
        if name in data:
            value = data[name]
            print(f'У абонента "{name}" номер телефона: {value}')
        else:
            print(f'Контакт "{name}" в телефонном справочнике отсутствует')

#Сохраняем новый контакт
def save_contact():
    data = read_file()
    name = input("Введите имя контакта: ")
    number = input("Введите номер телефона без пробелов: ")
    data[name] = number
    print('Контакт добавлен!')
    write_file(data)

# Изменить контакт
#def change_contact():
    


save_contact()
print(read_file())


