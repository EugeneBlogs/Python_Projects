'''
Для перевода текста используется библиотека "googletrans" (version 3.1.0a0).
Для озвучки текста используется библиотека "pyttsx3".
'''


from tkinter import *
from tkinter import messagebox

from googletrans import Translator
translator = Translator()
import pyttsx3
engine = pyttsx3.init()

name_current_widget = ""

print("!!!")
print("В консоль будут выводится отчёты об ошибках. Чтобы консоль не открываласть - сохраните файл в формате '.pyw'.")
print("!!!")

window = Tk()
window.title("Переводчик на базе Google Translate")
window.geometry("820x350")

def copy_text():
    text = window.nametowidget(name_current_widget).get("1.0", "end")
    window.clipboard_clear()
    window.clipboard_append(text)

def copy_select_text():
    text = window.nametowidget(name_current_widget).selection_get()
    window.clipboard_clear()
    window.clipboard_append(text)

def paste_text():
    text = window.clipboard_get()
    window.nametowidget(name_current_widget).insert(INSERT, text)

m = Menu(window, tearoff=0)
m.add_command(label="Скопировать текст", command=copy_text)
m.add_command(label="Скопировать выделенный текст", command=copy_select_text)
m.add_command(label="Вставить текст", command=paste_text)

def context_menu(event):
    global name_current_widget
    try:
        name_current_widget = str(event.widget)
        m.tk_popup(event.x_root, event.y_root)
    finally:
        m.grab_release()

from_language = "Russian"
to_language = "English"
translate_logo = PhotoImage(file="./img/translate.png")
sound_logo = PhotoImage(file="./img/sound.png")

def change():
    global from_language
    global to_language
    from_language,to_language = to_language,from_language
    if from_language == "Russian":
        from_lbl.config(text="Русский")
        to_lbl.config(text="English")
    elif from_language == "English":
        from_lbl.config(text="English")
        to_lbl.config(text="Русский")

def translate():
    global translator
    try:
        from_lg = ""
        to_lg = ""
        if from_language == "Russian":
            from_lg = "ru"
            to_lg = "en"
        elif from_language == "English":
            from_lg = "en"
            to_lg = "ru"
        translation = translator.translate(from_text.get("1.0", "end"), src=from_lg, dest=to_lg).text
        to_text.config(state="normal")
        to_text.delete("1.0", END)
        to_text.insert("1.0", translation)
        to_text.config(state="disabled")
    except:
        messagebox.showerror("Ошибка", "Что-то пошло не так. Повторите попытку. Возможно, отсутствует соединение с интернетом.")

def sound(choose):
    text = ""
    voices = engine.getProperty('voices')
    if choose == "From":
        text = from_text.get("1.0", "end")
        if from_language == "Russian":
            engine.setProperty('voice', voices[0].id)
        elif from_language == "English":
            engine.setProperty('voice', voices[1].id)
    elif choose == "To":
        text = to_text.get("1.0", "end")
        if to_language == "Russian":
            engine.setProperty('voice', voices[0].id)
        elif to_language == "English":
            engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()


frame = Frame(
   window,
   padx = 10,
   pady = 10
)
frame.pack(expand=True)

from_lbl = Label(
   frame,
    text="Русский",
    font=("Courier New", 20)
)
from_lbl.grid(row=1, column=1, pady=10, padx=15)

change_btn = Button(
        frame,
        text="<=>",
        cursor="hand2",
        foreground="#ffffff",
        background="#000000",
        font=("Courier New", 20),
        width=3,
        command=lambda: change()
)
change_btn.grid(row=1, column=2, pady=10)

to_lbl = Label(
   frame,
    text="English",
    font=("Courier New", 20)
)
to_lbl.grid(row=1, column=3, pady=10, padx=15)

from_text = Text(
    frame,
    width=20,
    height=3,
    font=("Courier New", 20),
    name="from_txt"
)
from_text.grid(row=2, column=1, pady=10, padx=15)
from_text.bind("<Button-3>", context_menu)

to_text = Text(
    frame,
    width=20,
    height=3,
    font=("Courier New", 20),
    state="disabled",
    name="to_txt"
)
to_text.grid(row=2, column=3, pady=10, padx=15)
to_text.bind("<Button-3>", context_menu)

translate_btn = Button(
        frame,
        image = translate_logo,
        cursor="hand2",
        background="#ffffff",
        width=50,
        command=lambda: translate()
)
translate_btn.grid(row=2, column=2, pady=10)

sound_from_btn = Button(
        frame,
        image = sound_logo,
        cursor="hand2",
        background="#ffffff",
        width=50,
        command=lambda: sound("From")
)
sound_from_btn.grid(row=3, column=1, pady=10)

sound_to_btn = Button(
        frame,
        image = sound_logo,
        cursor="hand2",
        background="#ffffff",
        width=50,
        command=lambda: sound("To")
)
sound_to_btn.grid(row=3, column=3, pady=10)

window.mainloop()