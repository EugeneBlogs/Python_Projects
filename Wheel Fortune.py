from tkinter import *
from tkinter import messagebox
import random
from tkinter.messagebox import askyesno

print("!!!")
print("В консоль будут выводится отчёты об ошибках. Чтобы консоль не открывалась - сохраните файл в формате '.pyw'.")
print("!!!")

window = Tk()
window.title("Колесо фортуны")
window.geometry("650x500")

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

def cube():
    num = random.randint(1, 6)
    print(['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685'][num - 1])
    messagebox.showinfo("Результат", f'Выпало число {num}.')

def coin():
    num = random.randint(1, 2)
    if num == 1:
        messagebox.showinfo("Результат", f'Выпал ОРЁЛ.')
    elif num == 2:
        messagebox.showinfo("Результат", f'Выпала РЕШКА.')

def yn():
    num = random.randint(1, 2)
    if num == 1:
        messagebox.showinfo("Результат", f'Да.')
    elif num == 2:
        messagebox.showinfo("Результат", f'Нет.')

def ticket():
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    num3 = random.randint(0, 9)
    num4 = random.randint(0, 9)
    num5 = random.randint(0, 9)
    num6 = random.randint(0, 9)
    sum_left = num1 + num2 + num3
    sum_right = num4 + num5 + num6
    number = f"{num1}{num2}{num3}{num4}{num5}{num6}"
    if sum_left == sum_right:
        messagebox.showinfo("Результат", f'Билет №{number} оказался СЧАСТЛИВЫМ!')
    else:
        messagebox.showinfo("Результат", f'Билет №{number} оказался НЕСЧАСТЛИВЫМ.')

frame = Frame(
   window,
   padx = 10,
   pady = 10
)
frame.pack(expand=True)

text = Entry(
    frame,
    width=15,
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
        width=15,
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
        width=15,
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
        width=15,
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
        command=lambda: choose()
)
choose_btn.grid(row=3, column=1, columnspan=4, sticky=EW, pady=5)

random_btn = Button(
        frame,
        text="Расположить в случайном порядке",
        cursor="hand2",
        foreground="white",
        background="blue",
        font=("Cambria", 12),
        command=lambda: random_order()
)
random_btn.grid(row=4, column=1, columnspan=4, sticky=EW, pady=5)

cube_btn = Button(
        frame,
        text="Игральная кость",
        cursor="hand2",
        foreground="white",
        background="black",
        font=("Cambria", 10),
        width=25,
        command=lambda: cube()
)
cube_btn.grid(row=5, column=1, padx=5, pady=5)

coin_btn = Button(
        frame,
        text="Монетка",
        cursor="hand2",
        foreground="white",
        background="darkgoldenrod",
        font=("Cambria", 10),
        width=15,
        command=lambda: coin()
)
coin_btn.grid(row=5, column=2, padx=5, pady=5)

yn_btn = Button(
        frame,
        text="Да/Нет",
        cursor="hand2",
        foreground="white",
        background="mediumpurple",
        font=("Cambria", 10),
        width=15,
        command=lambda: yn()
)
yn_btn.grid(row=5, column=3, padx=5, pady=5)

ticket_btn = Button(
        frame,
        text="Билет",
        cursor="hand2",
        foreground="black",
        background="deeppink1",
        font=("Cambria", 10),
        width=15,
        command=lambda: ticket()
)
ticket_btn.grid(row=5, column=4, padx=5, pady=5)

checkbutton = Checkbutton(
    frame,
    text="Очищать поле автоматически",
    variable=enabled
)
checkbutton.grid(row=6, column=1, columnspan=4, pady=5)
checkbutton.select()

window.mainloop()
