'''
Для хранения заметок используется библиотека "pickleDB".
'''

from tkinter import *
from tkinter import messagebox, simpledialog, colorchooser
from tkinter.messagebox import askyesno

import pickledb
db = pickledb.load("notes.db", True)

current_row = 1
current_column = 1

print("!!!")
print("В консоль будут выводится отчёты об ошибках. Чтобы консоль не открываласть - сохраните файл в формате '.pyw'.")
print("!!!")

window = Tk()
window.title("Заметки")
window.geometry("900x770")
window.option_add("*tearOff", FALSE)
window.resizable(width=False, height=False)

def clear_extra_widgets():
    for widget in window.winfo_children():
        if widget not in global_widgets:
            widget.destroy()

def new_note():
    if len(db.getall()) < 20:
        color = str(colorchooser.askcolor(initialcolor="white"))
        color = color[color.find("'") + len("'"):].split()[0].replace("'", "").replace(")", "")
        color_to_text = "[({" + color + "})]"
        name = simpledialog.askstring(title="Название", prompt="Название заметки")
        all_notes = str(db.getall())
        all_notes = all_notes.replace("dict_keys([", "").replace("])", "").replace("'", "")
        notes = all_notes.split(", ")
        if name == "":
            messagebox.showerror("Ошибка", "Название не может быть пустым.")
        elif name in notes:
            messagebox.showerror("Ошибка", "Заметка с таким названем уже существует.")
        elif "," in name:
            messagebox.showerror("Ошибка", "Нельзя использовать данный символ в названии.")
        else:
            if name != None:
                text = simpledialog.askstring(title="Текст", prompt="Текст заметки")
                result_text = f"{color_to_text} {text}"
                if text != None:
                    try:
                        db.set(name, result_text)
                        messagebox.showinfo("Успешно", f"Заметка \"{name}\" с текстом \"{text}\" успешно создана!")
                        clear_extra_widgets()
                        create_notes()
                    except:
                        messagebox.showerror("Ошибка", "Что-то пошло не так. Повторите попытку.")
    else:
        messagebox.showerror("Ошибка", "Нельзя превысить лимит заметок. Максимальное количество - 20.")

def create_notes():
    try:
        global current_row
        global current_column
        current_row = 1
        current_column = 1

        all_notes = str(db.getall())
        all_notes = all_notes.replace("dict_keys([", "").replace("])", "").replace("'", "")
        notes = all_notes.split(", ")
        for i in notes:
            name = i
            text = db.get(name)
            symbols = []
            for symbol in text:
                symbols += symbol
            hex = f"#{symbols[4]}{symbols[5]}{symbols[6]}{symbols[7]}{symbols[8]}{symbols[9]}"
            text = text[14:]
            textbox = Text(
                window,
                width=20,
                height=10,
                font=("Bahnschrift", 12),
                background=hex,
            )
            textbox.insert("1.0", f"{name}\n\n{text}")
            textbox.config(state="disabled")
            textbox.grid(row=current_row, column=current_column)
            if current_column < 5:
                current_column += 1
            else:
                current_row += 1
                current_column = 1
    except:
        print("Созданных заметок ещё нет.")

def delete_note():
    name = simpledialog.askstring(title="Название", prompt="Название заметки")
    all_notes = str(db.getall())
    all_notes = all_notes.replace("dict_keys([", "").replace("])", "").replace("'", "")
    notes = all_notes.split(", ")
    if name in notes and name != "":
        if askyesno(title="Удалить заметку", message=f"Вы действительно хотите удалить заметку \"{name}\"?"):
            try:
                db.rem(name)
                messagebox.showwarning("Успешно", f"Заметка \"{name}\" удалена!")
            except:
                messagebox.showerror("Ошибка", "Что-то пошло не так. Повторите попытку.")
            clear_extra_widgets()
            create_notes()
    else:
        messagebox.showerror("Ошибка", "Заметка с таким названем не найдена.")

def delete_notes():
    if askyesno(title="Удалить все заметки", message=f"Вы действительно хотите удалить все заметки?"):
        try:
            db.deldb()
            messagebox.showwarning("Успешно", f"Заметки удалены!")
        except:
            messagebox.showerror("Ошибка", "Что-то пошло не так. Повторите попытку.")
    clear_extra_widgets()
    create_notes()

main_menu = Menu()
main_menu.add_cascade(label="Создать заметку", command=new_note)
del_menu = Menu()
del_menu.add_command(label="Заметку", command=delete_note)
del_menu.add_command(label="Все заметки", command=delete_notes)
main_menu.add_cascade(label="Удалить", menu=del_menu)

window.config(menu=main_menu)

global_widgets = window.winfo_children()

clear_extra_widgets()
create_notes()

window.mainloop()
