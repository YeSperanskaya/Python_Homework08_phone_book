# import csv
# from tkinter import Tk, Label, Entry, Button

# phone_book = {}

# def add_contact(name, number):
#     if name in phone_book:
#         return "Contact exists already"
#     else:
#         phone_book[name] = number
#         return "Contact added"

# def find_contact(name):
#     if name in phone_book:
#         return phone_book[name]
#     else:
#         return "Contact not found"

# def delete_contact(name):
#     if name in phone_book:
#         del phone_book[name]
#         return "Contact deleted"
#     else:
#         return "Contact not found"

# def save_contacts():
#     with open('book.csv', mode='w', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow(['Name', 'Number'])
#         for name, number in phone_book.items():
#             writer.writerow([name, number])
#     return "Contact saved"

# def load_contacts():
#     phone_book.clear()
#     try:
#         with open('book.csv', mode ='r') as file:
#             reader = csv.reader(file)
#             next(reader)
#             for row in reader:
#                 name, number = rowphone_book[name] = number
#         return "Contacts uploaded"  

# def create_gui():
#     def add_button_clic():
#         name = name_entry.get()
#         number = number_entry.get()
#         result = add_contact(name, number)
#         result_label.config(test=result)

#     def find_button_clic():
#         name = name_entry.get()
#         result = find_contact(name)
#         result_label.config(text=result)    

#     def delete_button_click():
#         name = name_entry.get()
#         result = delete_contact(name)
#         result_label.config(text=result)

#     def save_button_click():
#         result = save_contacts()
#         result_label.config(text=result)

#     def load_button_click():
#         result = load_contacts()
#         result_label.config(text=result)

#     window = Tk()
#     window.title("Phone boock")

#     name_label = Label(window, text="Name: ")
#     name_label.pack()
#     name_entry = Entry(window)
#     name_entry.pack()

#     name_label = Label(window, text="Number: ")
#     name_label.pack()
#     name_entry = Entry(window)
#     name_entry.pack()

#     add_button = Button(window, text="Add", command=add_button_click)
#     add_button.pack()

#     find_button = Button(window, text="Find", command=find_button_click)
#     find_button.pack()

#     delete_button = Button(window, text="Delete", command=delete_button_click)
#     delete_button.pack()

#     save_button = Button(window, text="Save", command=save_button_click)
#     save_button.pack()

#     load_button = Button(window, text="Load", command=load_button_click)
#     load_button.pack()

#     result_label = Label(window, text="")
#     result_label.pack()

# create_gui()

