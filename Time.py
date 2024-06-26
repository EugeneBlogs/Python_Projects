'''
Для получения МОСКОВСКОГО времени используется библиотека "pytz".
Для отслеживания нажатия клавиши на клавиатуре используется библиотека "keyboard".
'''

#region Подключённые библиотеки

from tkinter import *
from tkinter import messagebox, ttk
from tkinter.ttk import Combobox

from datetime import datetime, timedelta

import pytz

import keyboard
import winsound

from time import sleep

#endregion


print("!!!")
print("В консоль будут выводится отчёты об ошибках. Чтобы консоль не открываласть - сохраните файл в формате '.pyw'.")
print("!!!")

def volume_zero():
    for i in range(50):
        keyboard.send("volume down")

def closed(event):
    volume_zero()
    raise SystemExit

window = Tk()
window.title("Время")
window.geometry("550x450")
window.resizable(width=False, height=False)
window.bind("<Destroy>", closed)

notebook = ttk.Notebook()
notebook.pack(expand=True, fill=BOTH)

volume_zero()
for i in range(10):
    keyboard.send("volume up")

#region Массивы с числами для часов, минут и секунд
    
hours = []
min_sec = []
for i in range(0, 24):
    if i < 10:
        str = f"0{i}"
        hours.append(str)
    else:
        hours.append(f"{i}")
for i in range(0, 60):
    if i < 10:
        str = f"0{i}"
        min_sec.append(str)
    else:
        min_sec.append(f"{i}")

#endregion

#region Создание вкладок

clock = Frame(notebook)
alarm = Frame(notebook)
timer = Frame(notebook)
stopwatch = Frame(notebook)

clock.pack(fill=BOTH, expand=True)
alarm.pack(fill=BOTH, expand=True)
timer.pack(fill=BOTH, expand=True)
stopwatch.pack(fill=BOTH, expand=True)

clock_logo = PhotoImage(file="./img/clock.png")
alarm_logo = PhotoImage(file="./img/alarm.png")
timer_logo = PhotoImage(file="./img/timer.png")
stopwatch_logo = PhotoImage(file="./img/stopwatch.png")

notebook.add(clock, text="Часы", image=clock_logo, compound=LEFT)
notebook.add(alarm, text="Будильник", image=alarm_logo, compound=LEFT)
notebook.add(timer, text="Таймер", image=timer_logo, compound=LEFT)
notebook.add(stopwatch, text="Секундомер", image=stopwatch_logo, compound=LEFT)

#endregion

#region Часы

difference = -1

clock_lbl = Label(
   clock,
   font=('Impact', 45)
)
clock_lbl.pack(anchor='center')
name_day_lbl = Label(
   clock,
   font=('Impact', 45),
   foreground="#f0f0f0"
)
name_day_lbl.pack(anchor='center', pady=30)
date_lbl = Label(
   clock,
   font=('Impact', 45)
)
date_lbl.pack(anchor='center')

def selected(event):
    global difference
    city = zones_combobox.get()
    if city == "Калининград (МКС-1)":
        difference = -1
    elif city == "Москва, Санкт-Петербург (МКС)":
        difference = 0
    elif city == "Астрахань, Саратов (МКС+1)":
        difference = 1
    elif city == "Оренбург, Тюмень (МКС+2)":
        difference = 2
    elif city == "Омск (МКС+3)":
        difference = 3
    elif city == "Новосибирск, Кемерово (МКС+4)":
        difference = 4
    elif city == "Иркутск, Бурятия (МКС+5)":
        difference = 5
    elif city == "Якутск, Забайкальский край (МКС+6)":
        difference = 6
    elif city == "Приморский край, Хабаровск (МКС+7)":
        difference = 7
    elif city == "Магадан, Сахалин (МКС+8)":
        difference = 8
    elif city == "Камчатка, Чукотский АО (МКС+9)":
        difference = 9

time_zones = ["Калининград (МКС-1)",
              "Москва, Санкт-Петербург (МКС)",
              "Астрахань, Саратов (МКС+1)",
              "Оренбург, Тюмень (МКС+2)",
              "Омск (МКС+3)",
              "Новосибирск, Кемерово (МКС+4)",
              "Иркутск, Бурятия (МКС+5)",
              "Якутск, Забайкальский край (МКС+6)",
              "Приморский край, Хабаровск (МКС+7)",
              "Магадан, Сахалин (МКС+8)",
              "Камчатка, Чукотский АО (МКС+9)"]
zones_combobox = Combobox(clock, values=time_zones, width=30, font=('Impact', 20), state="readonly")
zones_combobox.pack(anchor='center', pady=30)
zones_combobox.set("Калининград (МКС-1)")
zones_combobox.bind("<<ComboboxSelected>>", selected)

def time():
    day = ""
    data = ""
    moscow_time = datetime.now(pytz.timezone('Europe/Moscow'))
    date = moscow_time + timedelta(hours=difference)
    if date.strftime("%A") == "Monday":
        day = "Понедельник"
        name_day_lbl.config(background="darkred")
    elif date.strftime("%A") == "Tuesday":
        day = "Вторник"
        name_day_lbl.config(background="red")
    elif date.strftime("%A") == "Wednesday":
        day = "Среда"
        name_day_lbl.config(background="orange")
    elif date.strftime("%A") == "Thursday":
        day = "Четверг"
        name_day_lbl.config(background="greenyellow")
    elif date.strftime("%A") == "Friday":
        day = "Пятница"
        name_day_lbl.config(background="yellow")
    elif date.strftime("%A") == "Saturday":
        day = "Суббота"
        name_day_lbl.config(background="green")
    elif date.strftime("%A") == "Sunday":
        day = "Воскресенье"
        name_day_lbl.config(background="lightgreen")
    if date.month == 1:
        data = f"{date.day} января {date.year} года"
        date_lbl.config(background="cyan", foreground="blue")
    elif date.month == 2:
        data = f"{date.day} февраля {date.year} года"
        date_lbl.config(background="cyan", foreground="blue")
    elif date.month == 3:
        data = f"{date.day} марта {date.year} года"
        date_lbl.config(background="pink", foreground="green")
    elif date.month == 4:
        data = f"{date.day} апреля {date.year} года"
        date_lbl.config(background="pink", foreground="green")
    elif date.month == 5:
        data = f"{date.day} мая {date.year} года"
        date_lbl.config(background="pink", foreground="green")
    elif date.month == 6:
        data = f"{date.day} июня {date.year} года"
        date_lbl.config(background="yellow", foreground="lawngreen")
    elif date.month == 7:
        data = f"{date.day} июля {date.year} года"
        date_lbl.config(background="yellow", foreground="lawngreen")
    elif date.month == 8:
        data = f"{date.day} августа {date.year} года"
        date_lbl.config(background="yellow", foreground="lawngreen")
    elif date.month == 9:
        data = f"{date.day} сентября {date.year} года"
        date_lbl.config(background="orange", foreground="red")
    elif date.month == 10:
        data = f"{date.day} октября {date.year} года"
        date_lbl.config(background="orange", foreground="red")
    elif date.month == 11:
        data = f"{date.day} ноября {date.year} года"
        date_lbl.config(background="orange", foreground="red")
    elif date.month == 12:
        data = f"{date.day} декабря {date.year} года"
        date_lbl.config(background="cyan", foreground="blue")
    if date.hour == 22 or date.hour == 23 or date.hour == 0 or date.hour == 1 or date.hour == 2 or date.hour == 3 or date.hour == 4:
        clock_lbl.config(background="darkblue", foreground="lightblue")
    elif date.hour == 5 or date.hour == 6 or date.hour == 7 or date.hour == 8 or date.hour == 9 or date.hour == 10 or date.hour == 11:
        clock_lbl.config(background="goldenrod1", foreground="chartreuse")
    elif date.hour == 12 or date.hour == 13 or date.hour == 14 or date.hour == 15 or date.hour == 16:
        clock_lbl.config(background="white", foreground="cyan")
    elif date.hour == 17 or date.hour == 18 or date.hour == 19 or date.hour == 20 or date.hour == 21:
        clock_lbl.config(background="blue", foreground="azure4")
    string = date.strftime(f'%H:%M:%S')
    clock_lbl.config(text=string)
    name_day_lbl.config(text=day)
    date_lbl.config(text=data)
    clock_lbl.after(1000, time)

time()

#endregion

#region Будильник

def set_alarm():
    isWorked = True
    alarm_time = f"{alarm_hours_combobox.get()}:{alarm_minutes_combobox.get()}:{alarm_seconds_combobox.get()}"
    actual_time = datetime.now().strftime("%H:%M:%S")
    while actual_time != alarm_time:
        actual_time = datetime.now().strftime("%H:%M:%S")
        window.title(f"{actual_time} // {alarm_time}")
        if keyboard.is_pressed('esc'):
            isWorked = False
            break
    if isWorked:
        winsound.PlaySound("./files/alarm.wav", winsound.SND_ASYNC)
        messagebox.showinfo(alarm_time, "Сработал будильник!")
    window.title("Время")

info_lbl = Label(
   alarm,
   font=('Impact', 30),
    text="Установите время:"
)
info_lbl.pack(side=TOP, pady=5)
warning_lbl = Label(
   alarm,
   font=('Impact', 20),
    foreground="red",
    text='ВНИМАНИЕ! Время устанавливается по часовому поясу, установленному в системе компьютера.',
    wraplength=450
)
warning_lbl.pack(side=TOP, pady=5)
warning_lbl = Label(
   alarm,
   font=('Impact', 20),
    foreground="orange",
    text='ВНИМАНИЕ! Нажмите "Esc", чтобы остановить таймер.',
    wraplength=450
)
warning_lbl.pack(side=TOP, pady=5)
set_btn = Button(
    alarm,
    text="Установить будильник",
    font=('Impact', 15),
    cursor="hand2",
    foreground="black",
    background="yellow",
    command=lambda: set_alarm()
)
set_btn.pack(side=TOP, pady=15)
info_lbl = Label(
   alarm,
   font=('Impact', 15),
    text="Часы"
)
info_lbl.pack(side=LEFT, padx=7)
alarm_hours_combobox = Combobox(alarm, values=hours, width=5, font=('Impact', 15), state="readonly")
alarm_hours_combobox.pack(side=LEFT, padx=7)
alarm_hours_combobox.set("00")
info_lbl = Label(
   alarm,
   font=('Impact', 15),
    text="Минуты"
)
info_lbl.pack(side=LEFT, padx=7)
alarm_minutes_combobox = Combobox(alarm, values=min_sec, width=5, font=('Impact', 15), state="readonly")
alarm_minutes_combobox.pack(side=LEFT, padx=7)
alarm_minutes_combobox.set("00")
info_lbl = Label(
   alarm,
   font=('Impact', 15),
    text="Секунды"
)
info_lbl.pack(side=LEFT, padx=7)
alarm_seconds_combobox = Combobox(alarm, values=min_sec, width=5, font=('Impact', 15), state="readonly")
alarm_seconds_combobox.pack(side=LEFT, padx=7)
alarm_seconds_combobox.set("00")

#endregion

#region Таймер

def set_timer():
    timer_btn.config(state="disabled")
    isWorked = True
    temp = int(timer_hours_combobox.get()) * 3600 + int(timer_minutes_combobox.get()) * 60 + int(timer_seconds_combobox.get())
    while temp > -1:
        if keyboard.is_pressed('esc'):
            isWorked = False
            break
        mins, secs = divmod(temp, 60)
        hours = 0
        if mins > 60:
            hours, mins = divmod(mins, 60)
        hour_number = "{:2d}".format(hours)
        minute_number = "{:2d}".format(mins)
        second_number = "{:2d}".format(secs)
        if int(hour_number) < 10: hour_number = f"0{hour_number}".replace(" ", "")
        if int(minute_number) < 10: minute_number = f"0{minute_number}".replace(" ", "")
        if int(second_number) < 10: second_number = f"0{second_number}".replace(" ", "")
        count_lbl.config(text=f"{hour_number}:{minute_number}:{second_number}")
        window.update()
        sleep(1)
        if temp == 0 and isWorked:
            winsound.PlaySound("./files/alarm.wav", winsound.SND_ASYNC)
            messagebox.showinfo("Таймер", "Время вышло!")
        temp -= 1
    timer_btn.config(state="normal")

info_lbl = Label(
   timer,
   font=('Impact', 30),
    text="Установите время:"
)
info_lbl.pack(side=TOP, pady=5)
warning_lbl = Label(
   timer,
   font=('Impact', 20),
    foreground="orange",
    text='ВНИМАНИЕ! Нажмите "Esc", чтобы остановить таймер.',
    wraplength=450
)
warning_lbl.pack(side=TOP, pady=5)
count_lbl = Label(
   timer,
   font=('Impact', 40),
    foreground="red",
    text='00:00:00',
    wraplength=450
)
count_lbl.pack(side=TOP, pady=5)
timer_btn = Button(
    timer,
    text="Запустить таймер",
    font=('Impact', 15),
    cursor="hand2",
    foreground="white",
    background="green",
    name="timer_btn",
    command=lambda: set_timer()
)
timer_btn.pack(side=TOP, pady=15)
info_lbl = Label(
   timer,
   font=('Impact', 15),
    text="Часы"
)
info_lbl.pack(side=LEFT, padx=7)
timer_hours_combobox = Combobox(timer, values=hours, width=5, font=('Impact', 15), state="readonly")
timer_hours_combobox.pack(side=LEFT, padx=7)
timer_hours_combobox.set("00")
info_lbl = Label(
   timer,
   font=('Impact', 15),
    text="Минуты"
)
info_lbl.pack(side=LEFT, padx=7)
timer_minutes_combobox = Combobox(timer, values=min_sec, width=5, font=('Impact', 15), state="readonly")
timer_minutes_combobox.pack(side=LEFT, padx=7)
timer_minutes_combobox.set("00")
info_lbl = Label(
   timer,
   font=('Impact', 15),
    text="Секунды"
)
info_lbl.pack(side=LEFT, padx=7)
timer_seconds_combobox = Combobox(timer, values=min_sec, width=5, font=('Impact', 15), state="readonly")
timer_seconds_combobox.pack(side=LEFT, padx=7)
timer_seconds_combobox.set("00")

#endregion

#region Секундомер

isRun = False
moments = 0
moments_lap = 0
now_lap = "00:00:00"
laps = []

def start_stopwatch():
    global isRun
    global moments
    global moments_lap
    global now_lap
    isRun = True

    while isRun:

        mins, secs = divmod(moments, 60)
        hours = 0
        if mins > 60:
            hours, mins = divmod(mins, 60)
        hour_number = "{:2d}".format(hours)
        minute_number = "{:2d}".format(mins)
        second_number = "{:2d}".format(secs)
        if int(hour_number) < 10: hour_number = f"0{hour_number}".replace(" ", "")
        if int(minute_number) < 10: minute_number = f"0{minute_number}".replace(" ", "")
        if int(second_number) < 10: second_number = f"0{second_number}".replace(" ", "")
        stopwatch_lbl.config(text=f"{hour_number}:{minute_number}:{second_number}")

        mins_l, secs_l = divmod(moments_lap, 60)
        hours_l = 0
        if mins_l > 60:
            hours_l, mins_l = divmod(mins_l, 60)
        hour_number_l = "{:2d}".format(hours_l)
        minute_number_l = "{:2d}".format(mins_l)
        second_number_l = "{:2d}".format(secs_l)
        if int(hour_number_l) < 10: hour_number_l = f"0{hour_number_l}".replace(" ", "")
        if int(minute_number_l) < 10: minute_number_l = f"0{minute_number_l}".replace(" ", "")
        if int(second_number_l) < 10: second_number_l = f"0{second_number_l}".replace(" ", "")
        now_lap = f"{hour_number_l}:{minute_number_l}:{second_number_l}"

        window.update()
        sleep(1)
        moments += 1
        moments_lap += 1

def stop_stopwatch():
    global isRun
    isRun = False

def reset_stopwatch():
    stop_stopwatch()
    global moments
    global moments_lap
    global now_lap
    global laps
    moments = 0
    moments_lap = 0
    now_lap = "00:00:00"
    laps = []
    stopwatch_lbl.config(text="00:00:00")

def create_lap():
    global moments_lap
    global laps
    if isRun:
        laps.append(now_lap)
        moments_lap = 0
        winsound.PlaySound("./files/tick.wav", winsound.SND_ASYNC)

def show_laps():
    if isRun == False:
        string = ""
        for i in range(len(laps)):
            string += f"{i+1}. {laps[i]}\n"
        messagebox.showinfo("Круги", string)

stopwatch_lbl = Label(
   stopwatch,
   font=('Impact', 45),
    foreground="orange",
    text='00:00:00',
    wraplength=450
)
stopwatch_lbl.pack(side=TOP, pady=30)
start_btn = Button(
    stopwatch,
    text="Старт",
    font=('Impact', 15),
    cursor="hand2",
    foreground="white",
    background="lawngreen",
    width="6",
    command=lambda: start_stopwatch()
)
start_btn.pack(side=LEFT, padx=7)
stop_btn = Button(
    stopwatch,
    text="Стоп",
    font=('Impact', 15),
    cursor="hand2",
    foreground="white",
    background="red",
    width="6",
    command=lambda: stop_stopwatch()
)
stop_btn.pack(side=LEFT, padx=7)
reset_btn = Button(
    stopwatch,
    text="Перезапуск",
    font=('Impact', 15),
    cursor="hand2",
    foreground="black",
    background="yellow",
    width="10",
    command=lambda: reset_stopwatch()
)
reset_btn.pack(side=LEFT, padx=7)
lap_btn = Button(
    stopwatch,
    text="Круг",
    font=('Impact', 15),
    cursor="hand2",
    foreground="white",
    background="blue",
    width="7",
    command=lambda: create_lap()
)
lap_btn.pack(side=LEFT, padx=7)
show_btn = Button(
    stopwatch,
    text="Показать круги",
    font=('Impact', 15),
    cursor="hand2",
    foreground="black",
    background="cyan",
    width="15",
    command=lambda: show_laps()
)
show_btn.pack(side=LEFT, padx=7)

#endregion

window.mainloop()
