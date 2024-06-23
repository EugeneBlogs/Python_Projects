'''
Для создания QR-кодов используется библиотека "qrcode".
Для определения стандартного пути (C:/Users/...) используется библиотека "os".
'''

from tkinter import *
from tkinter import messagebox, simpledialog

import qrcode

import os
path = os.path.expanduser('~')

window = Tk()
window.withdraw()
text = simpledialog.askstring(title="Текст", prompt="Текст QR-кода")
if text == None:
    raise SystemExit
name = simpledialog.askstring(title="Название файла", prompt="Название файла")
if name == None:
    raise SystemExit
img = qrcode.make(text)
resilt_path = f"{path}\\Downloads\\{name}.png"
img.save(resilt_path)
messagebox.showinfo("Успешно", f"QR-код с текстом \"{text}\" сохранён по адресу \"{resilt_path}\".")