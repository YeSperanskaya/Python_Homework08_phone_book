# # на Отлично в одного человека надо сделать консольное приложение Телефонный 
# # справочник с внешним хранилищем информации, и чтоб был реализован основной 
# # функционал - просмотр, сохранение, импорт, поиск, удаление, изменение данных.

# # импорт нужной программы

# import json



# # просмотр
# def read_file():
#     f = open('phone_book.json', 'r')
#     f.read()



# # сохранение
# def save():
#     with open("phone_book.json", "w", encoding="utf-8") as doc:
#         doc.write(json.dumps(phone_book, ensure_ascii=False))
#     print("")
# # импорт

# # поиск
# #print("c" in the_dict)

# #удаление
# #del phone_book[name]

# # изменение данных
# #phone_book[name] = num

# # создание файла словаря:
# phone_book = dict()

# with open('phone_book.json', 'w') as file:
#     json.dump(phone_book, file)

# print(read_file())
# save_file()
# print(read_file())





# import json



# phonebook = {"Дядя Ваня": {'phones': [8311654654, 89654515],
#                            'birthday': "05.05.1990", 'email': "12@ya.ru"},
#              "Дядя Вася": {'phones' : [54654541]}
#              }

# def save():
#     with open("phoneNumber.json", "w", encoding="utf-8") as doc:
#         doc.write(json.dumps(phonebook, ensure_ascii=False))
#     print("")

# def load():
#     with open("phoneNumber.json", "r", encoding="utf-8") as doc:
#         telephone = json.load(doc)
#     print("")
#     return telephone


# print(phonebook['Дядя Ваня'])
# # print(phonebook['Дядя Ваня']['phones'])
# # print(phonebook['Дядя Ваня']['phones'][0])

# for name, values in phonebook.items():
#     print(name, values)
# print("Открыт телефонный справочник")

# try:
#     load()
# except:
#     phonebook = {"Дядя Ваня": {'phones': [8311654654, 89654515],
#                                'birthday': "05.05.1990", 'email': "12@ya.ru"},
#                  "Дядя Вася": {'phones': [54654541]}
#                  }

# while True:
#     command = input("Введите команду ")
#     if (command == "/exit"):
#         break
#     elif command == "/load":
#         phonebook = load()
#     elif command == "/save":
#         save()
#         print("Новая запись добавлена")
#     elif command == "/all":
#         print("Текущий телефонный список")
#         print(phonebook)
#     elif command == "/add":
#         name = input("Введите имя: ")
#         email = input("Введите EMAIL: ")
#         phone = input("Введите номера телефонов через пробел: ").split()
#         if phone != "":
#             phonebook[name] = phone
#         else:
#             continue
#     else:
#         print("Вы ввели не верную комманду, изучите мануал!")




name = "Михаил"
contact = { name : {'phones': [83122114654,896100115],
                       'birthday': "01.04.1991", 'email': "1rerer2@ya.ru"} }

def add():
    print(" ")
    phonebook[name] = contact
    
    
def save():
    with open("contants.json", "w", encoding="utf-8") as fh:
        fh.write(json.dumps(phonebook, ensure_ascii=False))
        
def show():
    for name, values in phonebook.items():
        print(name, values)

def load():
    try:
        with open("contants.json", "r", encoding="utf-8") as fh:
            temp_contacts = json.loads(fh.read())
    except:
        print("Загрузка тестового телефонного справочника")
        temp_contacts = {"Дядя Ваня": {'phones': [8311654654, 89654515],
                                   'birthday': "05.05.1990", 'email': "12@ya.ru"},
                     "Дядя Вася": {'phones': [54654541]}
                     }
    return temp_contacts

commands = { "add": add(), "save": save(), "show": show() }
phonebook = load()
print("Вам доступны следующие команды: ", *commands)


while True:
    command = input("Введите команду: ")
    try:
        commands[command]
    except:
        print("Неверная комманда")

