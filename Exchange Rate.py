'''
Для получения текущего курса используется библиотека "Кequests".
Чтобы ёё установить, напишите в командной строке команду "pip install requests".

Для отображения статуса загрузки данных используется библиотека "Rich".
Чтобы ёё установить, напишите в командной строке команду "pip install rich".

Если командная строка выдаёт ошибку, сделайте следующие действия:
1. Откройте "Изменение системных переменных среды".
2. Откройте "Переменные среды".
3. Выберите "Path" и нажмите "Изменить".
4. Создайте 2 ссылки: "C:/Users/mylni/AppData/Local/Programs/Python/Python312" и "C:/Users/mylni/AppData/Local/Programs/Python/Python312/Scripts" (ссылки немного могут отличаться).
'''

from rich.console import Console

import requests

from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox

import webbrowser

console = Console()

try:
    with console.status(f"[bold green]Загрузка данных ...[/bold green]") as status:
        st_accept = "text/html"
        headers = {
            "Accept": st_accept
        }
        request_dollar = requests.get(
            "https://www.banki.ru/products/currency/usd/?ysclid=lxlwjyi46d368077000", headers)
        src_dollar = request_dollar.text
        print("Курс доллара получен ✓")
        request_euro = requests.get(
            "https://www.banki.ru/products/currency/eur/?ysclid=lxlwynupj5785684786", headers)
        src_euro = request_euro.text
        print("Курс евро получен ✓")
        request_funt = requests.get(
            "https://www.banki.ru/products/currency/gbp/?ysclid=lxlxw32q78674110939", headers)
        src_funt = request_funt.text
        print("Курс фунта получен ✓")
        request_zlot = requests.get(
            "https://www.banki.ru/products/currency/pln/?ysclid=lxlwyskp4x408665150", headers)
        src_zlot = request_zlot.text
        print("Курс злотого получен ✓")
        request_yuan = requests.get(
            "https://www.banki.ru/products/currency/cny/?ysclid=lxlxw64sjc29349328", headers)
        src_yuan = request_yuan.text
        print("Курс юаня получен ✓")
        request_tenge = requests.get("https://www.banki.ru/products/currency/kzt/?ysclid=lxlywfex9a725827682", headers)
        src_tenge = request_tenge.text
        print("Курс тенге получен ✓")
        request_belorus = requests.get("https://www.banki.ru/products/currency/byn/?ysclid=lxm3cd2g6c843406242", headers)
        src_belorus = request_belorus.text
        print("Курс белорусского рубля получен ✓")

        after = '<div data-test="text" class="Text__sc-j452t5-0 bCCQWi">'
        print("")
        
        dollar = src_dollar[src_dollar.find(after)+len(after):].split()[0]
        dollar = dollar.replace(",", ".")
        dollar = float(dollar)
        print("Курс доллара обработан ✓")
        euro = src_euro[src_euro.find(after)+len(after):].split()[0]
        euro = euro.replace(",", ".")
        euro = float(euro)
        print("Курс евро обработан ✓")
        funt = src_funt[src_funt.find(after)+len(after):].split()[0]
        funt = funt.replace(",", ".")
        funt = float(funt)
        print("Курс фунта обработан ✓")
        zlot = src_zlot[src_zlot.find(after)+len(after):].split()[0]
        zlot = zlot.replace(",", ".")
        zlot = float(zlot)
        print("Курс злотого обработан ✓")
        yuan = src_yuan[src_yuan.find(after)+len(after):].split()[0]
        yuan = yuan.replace(",", ".")
        yuan = float(yuan)
        print("Курс юаня обработан ✓")
        tenge = src_tenge[src_tenge.find(after)+len(after):].split()[0]
        tenge = tenge.replace(",", ".")
        tenge = float(tenge)
        print("Курс тенге обработан ✓")
        belorus = src_belorus[src_belorus.find(after)+len(after):].split()[0]
        belorus = belorus.replace(",", ".")
        belorus = float(belorus)
        print("Курс белорусского рубля обработан ✓")
except:
    messagebox.showerror(title="Ошибка", message="Что-то пошло не так. Возможно, отсутствует подключение к интернету, либо на сайте \"Банки.Ру\" возникли проблемы.")
    raise SystemExit

print("")
print("!!!")
print("В консоль будут выводится отчёты об ошибках. Чтобы консоль не открывалась - сохраните файл в формате '.pyw'.")
print("!!!")

window = Tk()
window.title(f"Курс валют")
window.geometry("700x400")
window.option_add("*tearOff", FALSE)

def current_couse():
    messagebox.showinfo('Результат', f'1$ = {dollar}₽\n1€ = {euro}₽\n1£ = {funt}₽\n1zł = {zlot}₽\n1¥ = {yuan}₽\n1₸ = {tenge}₽\n1Br = {belorus}₽')

def siteUSD():
    webbrowser.open('https://www.banki.ru/products/currency/usd/?ysclid=lxlwjyi46d368077000', new=2)
def siteEUR():
    webbrowser.open('https://www.banki.ru/products/currency/eur/?ysclid=lxlwynupj5785684786', new=2)
def siteGBR():
    webbrowser.open('https://www.banki.ru/products/currency/gbp/?ysclid=lxlxw32q78674110939', new=2)
def sitePLN():
    webbrowser.open('https://www.banki.ru/products/currency/pln/?ysclid=lxlwyskp4x408665150', new=2)
def siteCNY():
    webbrowser.open('https://www.banki.ru/products/currency/cny/?ysclid=lxlxw64sjc29349328', new=2)
def siteKZT():
    webbrowser.open('https://www.banki.ru/products/currency/byn/?ysclid=lxm3cd2g6c843406242', new=2)
def siteBYN():
    webbrowser.open('https://www.banki.ru/products/currency/byn/?ysclid=lxm3cd2g6c843406242', new=2)

def selected_from(event):
    combobox_to.set("Российский Рубль (RUB)")

def selected_to(event):
    combobox_from.set("Российский Рубль (RUB)")

def convert():
    from_currency = combobox_from.get()
    to_currency = combobox_to.get()
    number = float(number_ent.get())
    if from_currency == "Российский Рубль (RUB)":
        if to_currency == "Российский Рубль (RUB)":
            result = number
            messagebox.showinfo('Результат', f'{number}₽ = {result}₽')
        elif to_currency == "Доллар (USD)":
            result = number / dollar
            result = round(result, 1)
            messagebox.showinfo('Результат', f'{number}₽ = {result}$')
        elif to_currency == "Евро (EUR)":
            result = number / euro
            result = round(result, 1)
            messagebox.showinfo('Результат', f'{number}₽ = {result}€')
        elif to_currency == "Британский Фунт Стерлингов (GBR)":
            result = number / funt
            result = round(result, 1)
            messagebox.showinfo('Результат', f'{number}₽ = {result}£')
        elif to_currency == "Польский Злотый (PLN)":
            result = number / zlot
            result = round(result, 1)
            messagebox.showinfo('Результат', f'{number}₽ = {result}zł')
        elif to_currency == "Китайский Юань (CNY)":
            result = number / yuan
            result = round(result, 1)
            messagebox.showinfo('Результат', f'{number}₽ = {result}¥')
        elif to_currency == "Казахстанский Тенге (KZT)":
            result = number / tenge
            result = round(result, 1)
            messagebox.showinfo('Результат', f'{number}₽ = {result}₸')
        elif to_currency == "Белорусский Рубль (BYN)":
            result = number / belorus
            result = round(result, 1)
            messagebox.showinfo('Результат', f'{number}₽ = {result}Br')
    elif to_currency == "Российский Рубль (RUB)":
        if from_currency == "Российский Рубль (RUB)":
            result = number
            messagebox.showinfo('Результат', f'{number}₽ = {result}₽')
        elif from_currency == "Доллар (USD)":
            result = number * dollar
            result = round(result, 1)
            messagebox.showinfo('Результат', f'{number}$ = {result}₽')
        elif from_currency == "Евро (EUR)":
            result = number * euro
            result = round(result, 1)
            messagebox.showinfo('Результат', f'{number}€ = {result}₽')
        elif from_currency == "Британский Фунт Стерлингов (GBR)":
            result = number * funt
            result = round(result, 1)
            messagebox.showinfo('Результат', f'{number}£ = {result}₽')
        elif from_currency == "Польский Злотый (PLN)":
            result = number * zlot
            result = round(result, 1)
            messagebox.showinfo('Результат', f'{number}zł = {result}₽')
        elif from_currency == "Китайский Юань (CNY)":
            result = number * yuan
            result = round(result, 1)
            messagebox.showinfo('Результат', f'{number}¥ = {result}₽')
        elif from_currency == "Казахстанский Тенге (KZT)":
            result = number * tenge
            result = round(result, 1)
            messagebox.showinfo('Результат', f'{number}₸ = {result}₽')
        elif from_currency == "Белорусский Рубль (BYN)":
            result = number * belorus
            result = round(result, 1)
            messagebox.showinfo('Результат', f'{number}Br = {result}₽')

currencies = ["Российский Рубль (RUB)",
           "Доллар (USD)",
           "Евро (EUR)",
           "Британский Фунт Стерлингов (GBR)",
           "Польский Злотый (PLN)",
           "Китайский Юань (CNY)",
           "Казахстанский Тенге (KZT)",
           "Белорусский Рубль (BYN)"]

frame = Frame(
   window,
   padx = 10,
   pady = 10
)
frame.pack(expand=True)

main_menu = Menu()
main_menu.add_cascade(label="Текущий курс", command=current_couse)
sites_menu = Menu()
sites_menu.add_command(label="Доллар", command=siteUSD)
sites_menu.add_command(label="Евро", command=siteEUR)
sites_menu.add_command(label="Британский Фунт Стерлингов", command=siteGBR)
sites_menu.add_command(label="Польский Злотый", command=sitePLN)
sites_menu.add_command(label="Китайский Юань", command=siteCNY)
sites_menu.add_command(label="Казахстанский Тенге", command=siteKZT)
sites_menu.add_command(label="Белорусский Рубль", command=siteBYN)
main_menu.add_cascade(label="Источник информации", menu=sites_menu)
window.config(menu=main_menu)

header_lbl = Label(
   frame,
   text="Курс валют",
    font=("Times New Roman", 20),
    fg="blue"
)
header_lbl.grid(row=1, column=2)

info_lbl = Label(
   frame,
   text='Информация получена с сайта "Банки.Ру"\nи обновляется при каждом запуске программы.',
    font=("Times New Roman", 12)
)
info_lbl.grid(row=2, column=2, pady=7)

number_lbl = Label(
   frame,
   text="Число",
   font=("Times New Roman", 16)
)
number_lbl.grid(row=3, column=1, pady=10)
number_ent = Entry(
    frame
)
number_ent.grid(row=3, column=3)

from_lbl = Label(
   frame,
   text="Из валюты",
    font=("Times New Roman", 16)
)
from_lbl.grid(row=4, column=1, pady=10)
combobox_from = Combobox(frame, values=currencies, width=30, state="readonly")
combobox_from.grid(row=4, column=3)
combobox_from.set("Российский Рубль (RUB)")
combobox_from.bind("<<ComboboxSelected>>", selected_from)


to_lbl = Label(
   frame,
   text="В валюту",
    font=("Times New Roman", 16)
)
to_lbl.grid(row=5, column=1, pady=10)
combobox_to = Combobox(frame, values=currencies, width=30, state="readonly")
combobox_to.grid(row=5, column=3)
combobox_to.set("Российский Рубль (RUB)")
combobox_to.bind("<<ComboboxSelected>>", selected_to)

calc_btn = Button(
        frame,
        text="Перевести",
        cursor="hand2",
        foreground="#00ff00",
        background="#008000",
        command=lambda: convert()
)
calc_btn.grid(row=6, column=2)

window.mainloop()
