from tkinter import *
from tkinter import messagebox
import random
from tkinter.messagebox import askyesno

print("!!!")
print("В консоль будут выводится отчёты об ошибках. Чтобы консоль не открываласть - сохраните файл в формате '.pyw'.")
print("!!!")

window = Tk()
window.title("Колесо фортуны")
window.geometry("550x450")

variants = []
enabled = IntVar()

def add():
    global variants
    listbox.insert(0, text.get())
    variants.append(text.get())
    if enabled.get() == 1:
        text.delete(0, END)

def delete():
    global variants
    try:
        selection = listbox.curselection()
        str = listbox.get(selection[0])
        listbox.delete(selection[0])
        variants.remove(str)
    except:
        messagebox.showerror("Ошибка", "Что-то пошло не так. Возможно, вы не выбрали элемент.")

def delete_all():
    global variants
    if askyesno(title="Очистить весь список", message=f"Вы действительно хотите очистить весь список?"):
        listbox.delete(0, 'end')
        variants = []
        if enabled.get() == 1:
            text.delete(0, END)

def choose():
    global variants
    try:
        messagebox.showinfo("Результат", f'Выбран элемент: "{random.choice(variants)}"')
    except:
        messagebox.showerror("Ошибка", "Что-то пошло не так. Возможно, вы не добавили элементы.")

def random_order():
    if len(variants) != 0:
        random.shuffle(variants)
        order = ""
        for i in range(len(variants)):
            order += f'{variants[i]}, '
        order = order[:-2]
        messagebox.showinfo("Результат", f'Порядок: "{order}"')
    else:
        messagebox.showerror("Ошибка", "Что-то пошло не так. Возможно, вы не добавили элементы.")



frame = Frame(
   window,
   padx = 10,
   pady = 10
)
frame.pack(expand=True)

text = Entry(
    frame,
    font=("Cambria", 14)
)
text.grid(row=1, column=1, padx=5, pady=5)

add_btn = Button(
        frame,
        text="Добавить",
        cursor="hand2",
        foreground="black",
        background="lawngreen",
        font=("Cambria", 10),
        width=10,
        command=lambda: add()
)
add_btn.grid(row=1, column=2, padx=5, pady=5)

delete_btn = Button(
        frame,
        text="Удалить",
        cursor="hand2",
        foreground="black",
        background="orange",
        font=("Cambria", 10),
        width=10,
        command=lambda: delete()
)
delete_btn.grid(row=1, column=3, padx=5, pady=5)

delete_all_btn = Button(
        frame,
        text="Удалить всё",
        cursor="hand2",
        foreground="black",
        background="red",
        font=("Cambria", 10),
        width=10,
        command=lambda: delete_all()
)
delete_all_btn.grid(row=1, column=4, padx=5, pady=5)

listbox = Listbox(
    frame,
    foreground="black",
    background="cyan",
    font=("Cambria", 15),
)
listbox.grid(row=2, column=1, columnspan=4, sticky=EW, pady=5)

choose_btn = Button(
        frame,
        text="Получить случайный элемент",
        cursor="hand2",
        foreground="black",
        background="yellow",
        font=("Cambria", 12),
        width=10,
        command=lambda: choose()
)
choose_btn.grid(row=3, column=1, columnspan=4, sticky=EW, pady=5)

random_btn = Button(
        frame,
        text="Расположить в слуяайном порядке",
        cursor="hand2",
        foreground="white",
        background="blue",
        font=("Cambria", 12),
        width=10,
        command=lambda: random_order()
)
random_btn.grid(row=4, column=1, columnspan=4, sticky=EW, pady=5)

checkbutton = Checkbutton(
    frame,
    text="Очищать поле автоматически",
    variable=enabled
)
checkbutton.grid(row=5, column=1, columnspan=4, pady=5)
checkbutton.select()

window.mainloop()
