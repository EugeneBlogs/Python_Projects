'''
Для создания QR-кодов используется библиотека "qrcode".
Для распознования QR-кодов используется библиотека "opencv-python".
'''

print("!!!")
print("В консоль будут выводится отчёты об ошибках. Чтобы консоль не открываласть - сохраните файл в формате '.pyw'.")
print("!!!")

from tkinter import *
from tkinter import messagebox, simpledialog, filedialog

import numpy as np
import qrcode
import cv2

window = Tk()
window.title("QR-коды")
window.geometry("230x50")
window.option_add("*tearOff", FALSE)
window.resizable(width=False, height=False)

def generate():
    root = Tk()
    root.withdraw()
    text = simpledialog.askstring(title="Текст", prompt="Текст QR-кода")
    if text != None:
        name = simpledialog.askstring(title="Название файла", prompt="Название файла")
    if name != None:
        img = qrcode.make(text)
        path = filedialog.askdirectory(title="Открыть папку", initialdir="/")
        if path:
            resilt_path = f"{path}/{name}.png"
            img.save(resilt_path)
            messagebox.showinfo("Успешно", f"QR-код с текстом \"{text}\" сохранён по адресу \"{resilt_path}\".")

def recognize():
    file_path = filedialog.askopenfilename()
    if file_path != "":
        stream = open(file_path, 'rb')
        bytes = bytearray(stream.read())
        array = np.asarray(bytes, dtype=np.uint8)
        img = cv2.imdecode(array, cv2.IMREAD_UNCHANGED)
        detector = cv2.QRCodeDetector()
        data, bbox, straight_qrcode = detector.detectAndDecode(img)
        if bbox is not None: messagebox.showinfo("Расшифровка", data)

def on_enter(e):
    e.widget['background'] = '#ffa500'
def on_leave_gen(e):
    e.widget['background'] = '#ff0000'
def on_leave_rec(e):
    e.widget['background'] = '#ffff00'

gen_btn = Button(
        window,
        text="Сгенерировать",
        cursor="hand2",
        foreground="#000000",
        background="#ff0000",
        command=lambda: generate()
)
gen_btn.grid(row=1, column=1, padx=15, pady=10)
gen_btn.bind("<Enter>", on_enter)
gen_btn.bind("<Leave>", on_leave_gen)

rec_btn = Button(
        window,
        text="Распознать",
        cursor="hand2",
        foreground="#000000",
        background="#ffff00",
        command=lambda: recognize()
)
rec_btn.grid(row=1, column=2, padx=15, pady=10)
rec_btn.bind("<Enter>", on_enter)
rec_btn.bind("<Leave>", on_leave_rec)

window.mainloop()
