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
        data = {}
        print(data)

# проверка чтения файла
read_file()



# блок команд связанный с добавлением нового контакта
# функция работы с файлом
def add_in_file():
    with open(file_phone_book, 'a') as f: # тут все равно добавляется элемент поэтому перезапись не нужна
        json.dump(phone_book, f)



# блок работы со списком
def add():
    name = input('Введите имя: ')
    phone = input('Введите номер телефона: ')
    phone_book[name] = phone
    print(f'Вами было введено имя: {name}, телефон: {phone}')
    add_in_file()

# тестовые команды
add()
read_file()

# команды для тг-бота 


