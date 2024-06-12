from tkinter import *
from tkinter import ttk
from tkinter import messagebox

print("!!!")
print("В консоль будут выводится отчёты об ошибках. Чтобы консоль не открываласть - сохраните файл в формате '.pyw'.")
print("!!!")

window = Tk()
window.title("Системы счисления")
window.geometry("460x300")

def changeFrom():
    to_spin.set(10)
def changeTo():
    from_spin.set(10)

frame = Frame(
   window,
   padx = 10,
   pady = 10
)
frame.pack(expand=True)

info_lbl = Label(
   frame,
   text="Системы счисления",
    font=("Calibri", 16)
)
info_lbl.grid(row=1, column=2, pady=10)

number_lbl = Label(
   frame,
   text="Число",
   font=("Calibri", 16)
)
number_lbl.grid(row=2, column=1, pady=10)
number_ent = Entry(
    frame
)
number_ent.grid(row=2, column=3)

from_lbl = Label(
   frame,
   text="Из системы",
    font=("Calibri", 16)
)
from_lbl.grid(row=3, column=1, pady=10)
from_spin = ttk.Spinbox(frame, from_=1, to=100, command=changeFrom, state="readonly")
from_spin.grid(row=3, column=3)


to_lbl = Label(
   frame,
   text="В систему",
    font=("Calibri", 16)
)
to_lbl.grid(row=4, column=1, pady=10)
to_spin = ttk.Spinbox(frame, from_=1, to=100, command=changeTo, state="readonly")
to_spin.grid(row=4, column=3)

calc_btn = Button(
        frame,
        text="Перевести",
        cursor="hand2",
        foreground="#7d0000",
        background="#ff0000",
        command=lambda: convert(number_ent.get(), from_spin.get(), to_spin.get())
)
calc_btn.grid(row=5, column=2)

def convert(number, from_system, to_system):
    number = int(number)
    from_system = int(from_system)
    to_system = int(to_system)
    result = 0
    if from_system == 10:
        result = from_ten(number, to_system)
    else:
        result = int(str(number), from_system)
    messagebox.showinfo('Результат', f'Число {number} из {from_system} системы счисления в {to_system} систему счисления = {result}.')


def from_ten(number, base, upper=False):
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    if base > len(digits): return None
    result = ''
    while number > 0:
        result = digits[number % base] + result
        number //= base
    return result.upper() if upper else result

window.mainloop()