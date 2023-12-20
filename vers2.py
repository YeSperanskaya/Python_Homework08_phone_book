import json

def main():
    # Открываем файл с данными
    file_name = 'phonebook.json'
    try:
        with open(file_name, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []

    print('Телефонный справочник:')
    print('- Сохранено записей: {}'.format(len(data)))
    print()

    # Просмотр записей
    for person in data:
        print(f'Имя: {person["name"]}, Телефон: {person["phone"]}')
        print()

    # Добавление записи
    name = input('Введите имя: ')
    phone = input('Введите номер телефона: ')

    data.append({'name': name, 'phone': phone})

    with open(file_name, 'w') as f:
        json.dump(data, f)


        print(f'\nЗапись добавлена: Имя: {name}, Телефон: {phone}')
        print()

#Удаление записи
def delete_record(person_name):
    for i, person in enumerate(data):
        if person['name'] == person_name:
            del data[i]
            break

def search_record(query):
    found_records = [person for person in data if person['name'].startswith(query)]
    if not found_records:
        return 'Запись не найдена'
    for record in found_records:
        print(f'{record["name"]} - {record["phone"]}')
        if name == 'main':
            main()

# В этом примере данные хранятся в JSON файле 'phonebook.json', который находится в текущей рабочей директории. Этот файл содержит список объектов, каждый из которых представляет запись в телефонной книге.

# Для просмотра всех записей используется цикл, который перебирает каждый объект в списке и выводит его имя и телефон.

# Добавление новой записи выполняется путем добавления нового объекта в список и перезаписи файла с данными.


# Удаление записи выполняется с использованием функции delete_record, которая принимает имя удаляемой записи и удаляет соответствующий элемент из списка.

# Поиск записи выполняется с помощью функции search_record, которая ищет записи, начинающиеся с введенного запроса. Если запись найдена, она выводится на экран, в противном случае выводится сообщение о том, что запись не найдена.

# Обратите внимание, что данный код является базовым примером работы с внешним JSON файлом и может быть расширен для поддержки более сложных операций и структурирования данных.