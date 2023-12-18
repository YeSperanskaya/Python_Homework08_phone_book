# на Отлично в одного человека надо сделать консольное приложение Телефонный справочник с внешним хранилищем информации, и чтоб был реализован основной функционал - просмотр, сохранение, импорт, поиск, удаление, изменение данных.

# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных




# # import csv
# # from tkinter import Tk, Label, Entry, Button

# # phone_book = {}

# # def add_contact(name, number):
# #     if name in phone_book:
# #         return "Contact exists already"
# #     else:
# #         phone_book[name] = number
# #         return "Contact added"

# # def find_contact(name):
# #     if name in phone_book:
# #         return phone_book[name]
# #     else:
# #         return "Contact not found"

# # def delete_contact(name):
# #     if name in phone_book:
# #         del phone_book[name]
# #         return "Contact deleted"
# #     else:
# #         return "Contact not found"

# # def save_contacts():
# #     with open('book.csv', mode='w', newline='') as file:
# #         writer = csv.writer(file)
# #         writer.writerow(['Name', 'Number'])
# #         for name, number in phone_book.items():
# #             writer.writerow([name, number])
# #     return "Contact saved"

# # def load_contacts():
# #     phone_book.clear()
# #     try:
# #         with open('book.csv', mode ='r') as file:
# #             reader = csv.reader(file)
# #             next(reader)
# #             for row in reader:
# #                 name, number = rowphone_book[name] = number
# #         return "Contacts uploaded"  

# # def create_gui():
# #     def add_button_clic():
# #         name = name_entry.get()
# #         number = number_entry.get()
# #         result = add_contact(name, number)
# #         result_label.config(test=result)

# #     def find_button_clic():
# #         name = name_entry.get()
# #         result = find_contact(name)
# #         result_label.config(text=result)    

# #     def delete_button_click():
# #         name = name_entry.get()
# #         result = delete_contact(name)
# #         result_label.config(text=result)

# #     def save_button_click():
# #         result = save_contacts()
# #         result_label.config(text=result)

# #     def load_button_click():
# #         result = load_contacts()
# #         result_label.config(text=result)

# #     window = Tk()
# #     window.title("Phone boock")

# #     name_label = Label(window, text="Name: ")
# #     name_label.pack()
# #     name_entry = Entry(window)
# #     name_entry.pack()

# #     name_label = Label(window, text="Number: ")
# #     name_label.pack()
# #     name_entry = Entry(window)
# #     name_entry.pack()

# #     add_button = Button(window, text="Add", command=add_button_click)
# #     add_button.pack()

# #     find_button = Button(window, text="Find", command=find_button_click)
# #     find_button.pack()

# #     delete_button = Button(window, text="Delete", command=delete_button_click)
# #     delete_button.pack()

# #     save_button = Button(window, text="Save", command=save_button_click)
# #     save_button.pack()

# #     load_button = Button(window, text="Load", command=load_button_click)
# #     load_button.pack()

# #     result_label = Label(window, text="")
# #     result_label.pack()

# # create_gui()





import json


phonebook = {"Дядя Ваня": {'phones': [8311654654, 89654515],
                           'birthday': "05.05.1990", 'email': "12@ya.ru"},
             "Дядя Вася": {'phones' : [54654541]}
             }

def save():
    with open("phoneNumber.json", "w", encoding="utf-8") as doc:
        doc.write(json.dumps(phonebook, ensure_ascii=False))
    print("")

def load():
    with open("phoneNumber.json", "r", encoding="utf-8") as doc:
        telephone = json.load(doc)
    print("")
    return telephone


print(phonebook['Дядя Ваня'])
# print(phonebook['Дядя Ваня']['phones'])
# print(phonebook['Дядя Ваня']['phones'][0])

for name, values in phonebook.items():
    print(name, values)
print("Открыт телефонный справочник")

try:
    load()
except:
    phonebook = {"Дядя Ваня": {'phones': [8311654654, 89654515],
                               'birthday': "05.05.1990", 'email': "12@ya.ru"},
                 "Дядя Вася": {'phones': [54654541]}
                 }

while True:
    command = input("Введите команду ")
    if (command == "/exit"):
        break
    elif command == "/load":
        phonebook = load()
    elif command == "/save":
        save()
        print("Новая запись добавлена")
    elif command == "/all":
        print("Текущий телефонный список")
        print(phonebook)
    elif command == "/add":
        name = input("Введите имя: ")
        email = input("Введите EMAIL: ")
        phone = input("Введите номера телефонов через пробел: ").split()
        if phone != "":
            phonebook[name] = phone
        else:
            continue
    else:
        print("Вы ввели не верную комманду, изучите мануал!")