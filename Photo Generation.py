'''
Для отправки запроса на сервер используется библиотека "requests".
Для конвертации текста в фото используется библиотека "base64".
'''

print("!!!")
print("В консоль будут выводится отчёты об ошибках. Чтобы консоль не открывалась - сохраните файл в формате '.pyw'.")
print("!!!")

import json
import time
import requests
import base64
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox, filedialog

window = Tk()
window.title("Генерация фото")
window.geometry("650x550")
window.option_add("*tearOff", FALSE)

class Text2ImageAPI:
    def __init__(self, url, api_key, secret_key):
        self.URL = url
        self.AUTH_HEADERS = {
            'X-Key': f'Key {api_key}',
            'X-Secret': f'Secret {secret_key}',
        }
    def get_model(self):
        response = requests.get(self.URL + 'key/api/v1/models', headers=self.AUTH_HEADERS)
        data = response.json()
        return data[0]['id']
    def generate(self, prompt, model, images=1, width=1024, height=1024, style=3):
        styles = ["KANDINSKY", "UHD", "ANIME", "DEFAULT"]
        params = {
            "type": "GENERATE",
            "numImages": images,
            "width": width,
            "height": height,
            "style": styles[style],
            "generateParams": {
                "query": f"{prompt}"
            }
        }
        data = {
            'model_id': (None, model),
            'params': (None, json.dumps(params), 'application/json')
        }
        response = requests.post(self.URL + 'key/api/v1/text2image/run', headers=self.AUTH_HEADERS, files=data)
        data = response.json()
        return data['uuid']
    def check_generation(self, request_id, attempts=10, delay=10):
        while attempts > 0:
            response = requests.get(self.URL + 'key/api/v1/text2image/status/' + request_id, headers=self.AUTH_HEADERS)
            data = response.json()
            if data['status'] == 'DONE':
                return data['images']
            attempts -= 1
            time.sleep(delay)

frame = Frame(
   window,
   padx=10,
   pady=10
)
frame.pack(expand=True)

header_lbl = Label(
   frame,
   text="Генерация фото",
    font=("Arial", 20),
    fg="red"
)
header_lbl.grid(row=1, column=2, pady=10)

info_lbl = Label(
   frame,
   text="Опишите изображение,\nа нейросеть Sber Kandinsky создаст его\nпо данному описанию.",
    font=("Arial", 16)
)
info_lbl.grid(row=2, column=2)

lbl = Label(
   frame,
   text="Название фото",
    font=("Arial", 16),
    fg="blue"
)
lbl.grid(row=3, column=1, pady=30)
name_photo = Entry(
    frame,
    font=("Arial", 16),
    width=30
)
name_photo.grid(row=3, column=2)

formats = ["Квадрат", "Горизонтально", "Вертикально"]
lbl = Label(
   frame,
   text="Формат изображения",
    font=("Arial", 16),
    fg="blue"
)
lbl.grid(row=4, column=1, pady=10)
combobox_format = Combobox(frame, values=formats, width=30, font=("Arial", 16), state="readonly")
combobox_format.grid(row=4, column=2)

types = ["Кандинский", "Детальное фото", "Аниме", "Обычный"]
lbl = Label(
   frame,
   text="Тип изображения",
    font=("Arial", 16),
    fg="blue"
)
lbl.grid(row=5, column=1, pady=10)
combobox_type = Combobox(frame, values=types, width=30, font=("Arial", 16), state="readonly")
combobox_type.grid(row=5, column=2)

lbl = Label(
   frame,
   text="Описание фото",
    font=("Arial", 16),
    fg="blue"
)
lbl.grid(row=6, column=1, pady=10)
text_photo = Entry(
    frame,
    font=("Arial", 16),
    width=30
)
text_photo.grid(row=6, column=2)

gen_btn = Button(
        frame,
        text="Сгенерировать изображение",
        cursor="hand2",
        background="#00ff00",
        foreground="#000000",
        font=("Arial", 14),
        width=30,
        command=lambda: generate_request()
)
gen_btn.grid(row=7, column=2, pady=30)


def generate_request():
    name = name_photo.get()
    format = combobox_format.get()
    type = combobox_type.get()
    prompt = text_photo.get().lower()
    if name == "" or format == "" or type == "" or prompt == "":
        messagebox.showerror("Ошибка", f"Необходимо заполнить все поля!")
    else:
        width = 1024
        height = 1024
        if format == "Квадрат":
            width = 1024
            height = 1024
        elif format == "Горизонтально":
            width = 1920
            height = 1080
        elif format == "Вертикально":
            width = 1080
            height = 1920

        style = 3
        if type == "Кандинский":
            style = 0
        elif type == "Детальное фото":
            style = 1
        elif type == "Аниме":
            style = 2
        elif type == "Обычный":
            style = 3
        send_request(name, prompt, width, height, style)

def send_request(name, prompt, w, h, s):
    try:
        api = Text2ImageAPI('https://api-key.fusionbrain.ai/', '72AB335102A9D57C5A2440F9D724FEDA',
                            'CB4B5DD258A6F04C4BCB20F97BF2D20B')
        model_id = api.get_model()
        uuid = api.generate(prompt, model_id, style=s, width=w, height=h)
        images = api.check_generation(uuid)
        image_base64 = images[0]
        image_data = base64.b64decode(image_base64)
        path = filedialog.askdirectory(title="Открыть папку", initialdir="/")
        if path:
            resilt_path = f"{path}/{name}.png"
            with open(resilt_path, "wb") as file:
                file.write(image_data)
                gen_btn.text = "Сгенерировать изображение"
                messagebox.showinfo("Успешно", f"Изображение «{name}» сохранено по адресу «{path}».")
    except:
        messagebox.showerror("Ошибка", f"При генерации изображения произошла ошибка!")

window.mainloop()