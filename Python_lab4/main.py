from tkinter import *
from tkinter import filedialog
import tkinter.simpledialog as tkSimpleDialog
import tkinter.messagebox as message_box
import urllib.request
import json
from tkinter import scrolledtext


"""
Функция загрузки json файла по ссылке
"""

def load():
    try:
        url = tkSimpleDialog.askstring("", "Enter a url:")
        data = urllib.request.urlopen(url)
    except:
        message_box.showerror(title="Error", message="Wrong url")
    else:
        data = data.read().decode('utf-8')
        data = "".join(filter(str.strip, data.split('\r')))         # Убираем символ \r  
        text_box.delete('1.0', 'end')                               # Убираем то, что было напечатано
        text_box.insert('1.0', data)                                # Вставляем json файл


"""
Проверка json файла на ошибки
Вызывается в check() и в save_as()
"""
def is_JSON(data):
    try:
        json.loads(data)
    except ValueError as e:
        return False
    return True


"""
Проверка синтаксиса json файла
"""
def check():
    if is_JSON(text_box.get(1.0, END)):
        message_box.showinfo(title="Syntax checker", message="All good")
    else:
        message_box.showerror(title="Syntax checker", message="Invalid syntax")


"""
Сохранение файла в выбранной пользователем директории
"""
def save_as():
    if is_JSON(text_box.get(1.0, END)):
        file = filedialog.asksaveasfile(mode='w', defaultextension=".json", filetypes=[("json files", '*.json')])
        file.write(text_box.get(1.0, END))
    else:
        message_box.showerror(title="Syntax checker", message="Invalid syntax")


window = Tk()                                   # Запускаем Tkinter
window.geometry('800x600')                      # Задаём размеры
window.title("JSON Editor")                     # Даём название окну

menu = Menu(window)                             # Создаем меню
window.config(menu=menu)  

file_menu = Menu(menu)  

file_menu.add_command(label="Load", command=load)   # Загрузка JSON

file_menu.add_command(label="Check",command=check)  # Проверка синтаксиса json файла

file_menu.add_command(label="Save as", command=save_as) # Сохранение файла

text_box = Text(wrap=WORD)                             # Создаем техтовый блок
text_box.pack(side='left', fill='both', expand=True)   # Размещаем в главном окне и убираем отступы

scroll = Scrollbar(window)                          # Создаем полосу прокрутки
scroll.pack(side=LEFT, fill=Y)
text_box.config(yscrollcommand=scroll.set)

menu.add_cascade(label='File', menu=file_menu)  # Меню 

window.mainloop()                               # Работает пока не закроют
