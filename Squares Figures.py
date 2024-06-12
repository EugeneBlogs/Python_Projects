import math
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox

print("!!!")
print("В консоль будут выводится отчёты об ошибках. Чтобы консоль не открываласть - сохраните файл в формате '.pyw'.")
print("!!!")

window = Tk()
window.title("Калькулятор площадей фигур")
window.geometry("550x450")

def selected(event):
    selection = combobox.get()
    if selection == "Параллелограмм":
        figure_parallelogramm()
    elif selection == "Прямоугольник":
        figure_pryamougolnik()
    elif selection == "Квадрат":
        figure_kvadrat()
    elif selection == "Ромб":
        figure_romb()
    elif selection == "Трапеция":
        figure_trapecia()
    elif selection == "Треугольник":
        figure_treugolnik()
    elif selection == "Круг":
        figure_krug()
    elif selection == "Сектор":
        figure_sektor()
    elif selection == "Четырёхугольник":
        figure_4ugolnik()

def figure_parallelogramm():
    clear_extra_widgets()
    methods = ["Через основание и высоту",
               "Через смежные стороны и угол",
               "Через диагонали и угол"]
    method_combobox.config(values=methods, state="readonly")
    method_combobox.set("Через основание и высоту")
    method_combobox.bind("<<ComboboxSelected>>", selected_method_parallelogramm)
def selected_method_parallelogramm(event):
    selection = method_combobox.get()
    if selection == "Через основание и высоту":
        method_parallelogramm_storona_vysota()
    elif selection == "Через смежные стороны и угол":
        method_parallelogramm_storony_ugol()
    elif selection == "Через диагонали и угол":
        method_parallelogramm_diagonali_ugol()

def method_parallelogramm_storona_vysota():
    clear_extra_widgets()
    base_lbl = Label(
        frame,
        text="Основание",
        font=("Calibri", 16)
    )
    base_lbl.grid(row=5, column=1, pady=10)
    base_ent = Entry(
        frame
    )
    base_ent.grid(row=5, column=2)
    height_lbl = Label(
        frame,
        text="Высота",
        font=("Calibri", 16)
    )
    height_lbl.grid(row=6, column=1, pady=10)
    height_ent = Entry(
        frame
    )
    height_ent.grid(row=6, column=2)
    calc_btn = Button(
        frame,
        text="Рассчитать площадь",
        cursor="hand2",
        foreground="#006400",
        background="#00ff00",
        command=lambda: calc_pryamougolnik(base_ent.get(), height_ent.get())
    )
    calc_btn.grid(row=7, column=2)

def method_parallelogramm_storony_ugol():
    clear_extra_widgets()
    sideA_lbl = Label(
        frame,
        text="Сторона A",
        font=("Calibri", 16)
    )
    sideA_lbl.grid(row=5, column=1, pady=10)
    sideA_ent = Entry(
        frame
    )
    sideA_ent.grid(row=5, column=2)
    sideB_lbl = Label(
        frame,
        text="Сторона B",
        font=("Calibri", 16)
    )
    sideB_lbl.grid(row=6, column=1, pady=10)
    sideB_ent = Entry(
        frame
    )
    sideB_ent.grid(row=6, column=2)
    angle_lbl = Label(
        frame,
        text="Угол между ними (в °)",
        font=("Calibri", 16)
    )
    angle_lbl.grid(row=7, column=1, pady=10)
    angle_ent = Entry(
        frame
    )
    angle_ent.grid(row=7, column=2)
    calc_btn = Button(
        frame,
        text="Рассчитать площадь",
        cursor="hand2",
        foreground="#006400",
        background="#00ff00",
        command=lambda: calc_par_storony_ugol(sideA_ent.get(), sideB_ent.get(), angle_ent.get())
    )
    calc_btn.grid(row=8, column=2)
def calc_par_storony_ugol(sideA, sideB, angle):
    sideA = float(sideA)
    sideB = float(sideB)
    angle = float(angle)
    area = float(sideA * sideB * math.sin(convert_degrees_to_radians(angle)))
    show_result(area)

def method_parallelogramm_diagonali_ugol():
    clear_extra_widgets()
    diagonalA_lbl = Label(
        frame,
        text="Диагональ A",
        font=("Calibri", 16)
    )
    diagonalA_lbl.grid(row=5, column=1, pady=10)
    diagonalA_ent = Entry(
        frame
    )
    diagonalA_ent.grid(row=5, column=2)
    diagonalB_lbl = Label(
        frame,
        text="Диагональ B",
        font=("Calibri", 16)
    )
    diagonalB_lbl.grid(row=6, column=1, pady=10)
    diagonalB_ent = Entry(
        frame
    )
    diagonalB_ent.grid(row=6, column=2)
    angle_lbl = Label(
        frame,
        text="Угол между ними (в °)",
        font=("Calibri", 16)
    )
    angle_lbl.grid(row=7, column=1, pady=10)
    angle_ent = Entry(
        frame
    )
    angle_ent.grid(row=7, column=2)
    calc_btn = Button(
        frame,
        text="Рассчитать площадь",
        cursor="hand2",
        foreground="#006400",
        background="#00ff00",
        command=lambda: calc_treug_storony_ugol(diagonalA_ent.get(), diagonalB_ent.get(), angle_ent.get())
    )
    calc_btn.grid(row=8, column=2)


def figure_pryamougolnik():
    clear_extra_widgets()
    methods = ["Через смежные стороны"]
    method_combobox.config(values=methods, state="disabled")
    method_combobox.set("Через смежные стороны")
    clear_extra_widgets()
    sideA_lbl = Label(
        frame,
        text="Сторона A",
        font=("Calibri", 16)
    )
    sideA_lbl.grid(row=5, column=1, pady=10)
    sideA_ent = Entry(
        frame
    )
    sideA_ent.grid(row=5, column=2)
    sideB_lbl = Label(
        frame,
        text="Сторона B",
        font=("Calibri", 16)
    )
    sideB_lbl.grid(row=6, column=1, pady=10)
    sideB_ent = Entry(
        frame
    )
    sideB_ent.grid(row=6, column=2)
    calc_btn = Button(
        frame,
        text="Рассчитать площадь",
        cursor="hand2",
        foreground="#006400",
        background="#00ff00",
        command=lambda: calc_pryamougolnik(sideA_ent.get(), sideB_ent.get())
    )
    calc_btn.grid(row=7, column=2)
def calc_pryamougolnik(sideA, sideB):
    sideA = float(sideA)
    sideB = float(sideB)
    area = float(sideA * sideB)
    show_result(area)


def figure_kvadrat():
    clear_extra_widgets()
    methods = ["Через квадрат стороны",
               "Через квадрат диагонали"]
    method_combobox.config(values=methods, state="readonly")
    method_combobox.set("Через квадрат стороны")
    method_combobox.bind("<<ComboboxSelected>>", selected_method_kvadrat)
def selected_method_kvadrat(event):
    selection = method_combobox.get()
    if selection == "Через квадрат стороны":
        method_kvadrat_storona()
    elif selection == "Через квадрат диагонали":
        method_kvadrat_diagonal()

def method_kvadrat_storona():
    clear_extra_widgets()
    side_lbl = Label(
        frame,
        text="Сторона",
        font=("Calibri", 16)
    )
    side_lbl.grid(row=5, column=1, pady=10)
    side_ent = Entry(
        frame
    )
    side_ent.grid(row=5, column=2)
    calc_btn = Button(
        frame,
        text="Рассчитать площадь",
        cursor="hand2",
        foreground="#006400",
        background="#00ff00",
        command=lambda: calc_pryamougolnik(side_ent.get(), side_ent.get())
    )
    calc_btn.grid(row=6, column=2)
def method_kvadrat_diagonal():
    clear_extra_widgets()
    diagonal_lbl = Label(
        frame,
        text="Диагональ",
        font=("Calibri", 16)
    )
    diagonal_lbl.grid(row=5, column=1, pady=10)
    diagonal_ent = Entry(
        frame
    )
    diagonal_ent.grid(row=5, column=2)
    calc_btn = Button(
        frame,
        text="Рассчитать площадь",
        cursor="hand2",
        foreground="#006400",
        background="#00ff00",
        command=lambda: calc_treug_storona_vysota(diagonal_ent.get(), diagonal_ent.get())
    )
    calc_btn.grid(row=6, column=2)

def figure_romb():
    clear_extra_widgets()
    methods = ["Через диагонали"]
    method_combobox.config(values=methods, state="disabled")
    method_combobox.set("Через диагонали")
    diagonalA_lbl = Label(
        frame,
        text="Диагональ A",
        font=("Calibri", 16)
    )
    diagonalA_lbl.grid(row=5, column=1, pady=10)
    diagonalA_ent = Entry(
        frame
    )
    diagonalA_ent.grid(row=5, column=2)
    diagonalB_lbl = Label(
        frame,
        text="Диагональ B",
        font=("Calibri", 16)
    )
    diagonalB_lbl.grid(row=6, column=1, pady=10)
    diagonalB_ent = Entry(
        frame
    )
    diagonalB_ent.grid(row=6, column=2)
    calc_btn = Button(
        frame,
        text="Рассчитать площадь",
        cursor="hand2",
        foreground="#006400",
        background="#00ff00",
        command=lambda: calc_treug_storona_vysota(diagonalA_ent.get(), diagonalB_ent.get())
    )
    calc_btn.grid(row=7, column=2)


def figure_trapecia():
    clear_extra_widgets()
    methods = ["Через основания и высоту",
               "Через среднюю линюю"]
    method_combobox.config(values=methods, state="readonly")
    method_combobox.set("Через основания и высоту")
    method_combobox.bind("<<ComboboxSelected>>", selected_method_trapecia)
def selected_method_trapecia(event):
    selection = method_combobox.get()
    if selection == "Через основания и высоту":
        method_trapecia_osnovaniya()
    elif selection == "Через среднюю линюю":
        method_trapecia_sred()

def method_trapecia_osnovaniya():
    clear_extra_widgets()
    baseA_lbl = Label(
        frame,
        text="Основание A",
        font=("Calibri", 16)
    )
    baseA_lbl.grid(row=5, column=1, pady=10)
    baseA_ent = Entry(
        frame
    )
    baseA_ent.grid(row=5, column=2)
    baseB_lbl = Label(
        frame,
        text="Основание B",
        font=("Calibri", 16)
    )
    baseB_lbl.grid(row=6, column=1, pady=10)
    baseB_ent = Entry(
        frame
    )
    baseB_ent.grid(row=6, column=2)
    height_lbl = Label(
        frame,
        text="Высота",
        font=("Calibri", 16)
    )
    height_lbl.grid(row=7, column=1, pady=10)
    height_ent = Entry(
        frame
    )
    height_ent.grid(row=7, column=2)
    calc_btn = Button(
        frame,
        text="Рассчитать площадь",
        cursor="hand2",
        foreground="#006400",
        background="#00ff00",
        command=lambda: calc_trapecia(baseA_ent.get(), baseB_ent.get(), height_ent.get())
    )
    calc_btn.grid(row=8, column=2)
def calc_trapecia(baseA, baseB, height):
    baseA = float(baseA)
    baseB = float(baseB)
    height = float(height)
    area = float((baseA + baseB) / 2 * height)
    show_result(area)

def method_trapecia_sred():
    clear_extra_widgets()
    sred_lbl = Label(
        frame,
        text="Средняя линяя",
        font=("Calibri", 16)
    )
    sred_lbl.grid(row=5, column=1, pady=10)
    sred_ent = Entry(
        frame
    )
    sred_ent.grid(row=5, column=2)
    height_lbl = Label(
        frame,
        text="Высота",
        font=("Calibri", 16)
    )
    height_lbl.grid(row=6, column=1, pady=10)
    height_ent = Entry(
        frame
    )
    height_ent.grid(row=6, column=2)
    calc_btn = Button(
        frame,
        text="Рассчитать площадь",
        cursor="hand2",
        foreground="#006400",
        background="#00ff00",
        command=lambda: calc_pryamougolnik(sred_ent.get(), height_ent.get())
    )
    calc_btn.grid(row=7, column=2)


def figure_treugolnik():
    clear_extra_widgets()
    methods = ["Через основание и высоту",
               "Через смежные стороны и угол",
               "Формула Герона",
               "Через радиус вписанной окружности",
               "Через радиус описанной окружности"]
    method_combobox.config(values=methods, state="readonly")
    method_combobox.set("Через сторону и высоту")
    method_combobox.bind("<<ComboboxSelected>>", selected_method_treugolnik)
def selected_method_treugolnik(event):
    selection = method_combobox.get()
    if selection == "Через основание и высоту":
        method_treugolnik_storona_vysota()
    elif selection == "Через смежные стороны и угол":
        method_treugolnik_storony_ugol()
    elif selection == "Формула Герона":
        method_treugolnik_geron()
    elif selection == "Через радиус вписанной окружности":
        method_treugolnik_vpis_okr()
    elif selection == "Через радиус описанной окружности":
        method_treugolnik_opis_okr()

def method_treugolnik_storona_vysota():
    clear_extra_widgets()
    base_lbl = Label(
        frame,
        text="Основание",
        font=("Calibri", 16)
    )
    base_lbl.grid(row=5, column=1, pady=10)
    base_ent = Entry(
        frame
    )
    base_ent.grid(row=5, column=2)
    height_lbl = Label(
        frame,
        text="Высота",
        font=("Calibri", 16)
    )
    height_lbl.grid(row=6, column=1, pady=10)
    height_ent = Entry(
        frame
    )
    height_ent.grid(row=6, column=2)
    calc_btn = Button(
        frame,
        text="Рассчитать площадь",
        cursor="hand2",
        foreground="#006400",
        background="#00ff00",
        command=lambda: calc_treug_storona_vysota(base_ent.get(), height_ent.get())
    )
    calc_btn.grid(row=7, column=2)
def calc_treug_storona_vysota(base, height):
    base = float(base)
    height = float(height)
    area = float(base * height / 2)
    show_result(area)

def method_treugolnik_storony_ugol():
    clear_extra_widgets()
    sideA_lbl = Label(
        frame,
        text="Сторона A",
        font=("Calibri", 16)
    )
    sideA_lbl.grid(row=5, column=1, pady=10)
    sideA_ent = Entry(
        frame
    )
    sideA_ent.grid(row=5, column=2)
    sideB_lbl = Label(
        frame,
        text="Сторона B",
        font=("Calibri", 16)
    )
    sideB_lbl.grid(row=6, column=1, pady=10)
    sideB_ent = Entry(
        frame
    )
    sideB_ent.grid(row=6, column=2)
    angle_lbl = Label(
        frame,
        text="Угол между ними (в °)",
        font=("Calibri", 16)
    )
    angle_lbl.grid(row=7, column=1, pady=10)
    angle_ent = Entry(
        frame
    )
    angle_ent.grid(row=7, column=2)
    calc_btn = Button(
        frame,
        text="Рассчитать площадь",
        cursor="hand2",
        foreground="#006400",
        background="#00ff00",
        command=lambda: calc_treug_storony_ugol(sideA_ent.get(), sideB_ent.get(), angle_ent.get())
    )
    calc_btn.grid(row=8, column=2)
def calc_treug_storony_ugol(sideA, sideB, angle):
    sideA = float(sideA)
    sideB = float(sideB)
    angle = float(angle)
    area = float(sideA * sideB * math.sin(convert_degrees_to_radians(angle)) / 2)
    show_result(area)

def method_treugolnik_geron():
    clear_extra_widgets()
    sideA_lbl = Label(
        frame,
        text="Сторона A",
        font=("Calibri", 16)
    )
    sideA_lbl.grid(row=5, column=1, pady=10)
    sideA_ent = Entry(
        frame
    )
    sideA_ent.grid(row=5, column=2)
    sideB_lbl = Label(
        frame,
        text="Сторона B",
        font=("Calibri", 16)
    )
    sideB_lbl.grid(row=6, column=1, pady=10)
    sideB_ent = Entry(
        frame
    )
    sideB_ent.grid(row=6, column=2)
    sideC_lbl = Label(
        frame,
        text="Сторона C",
        font=("Calibri", 16)
    )
    sideC_lbl.grid(row=7, column=1, pady=10)
    sideC_ent = Entry(
        frame
    )
    sideC_ent.grid(row=7, column=2)
    calc_btn = Button(
        frame,
        text="Рассчитать площадь",
        cursor="hand2",
        foreground="#006400",
        background="#00ff00",
        command=lambda: calc_treug_geron(sideA_ent.get(), sideB_ent.get(), sideC_ent.get())
    )
    calc_btn.grid(row=8, column=2)
def calc_treug_geron(sideA, sideB, sideC):
    sideA = float(sideA)
    sideB = float(sideB)
    sideC = float(sideC)
    poluperimetr = (sideA + sideB + sideC) / 2
    area = float(math.sqrt(poluperimetr*(poluperimetr-sideA)*(poluperimetr-sideB)*(poluperimetr-sideC)))
    show_result(area)

def method_treugolnik_vpis_okr():
    clear_extra_widgets()
    sideA_lbl = Label(
        frame,
        text="Сторона A",
        font=("Calibri", 16)
    )
    sideA_lbl.grid(row=5, column=1, pady=10)
    sideA_ent = Entry(
        frame
    )
    sideA_ent.grid(row=5, column=2)
    sideB_lbl = Label(
        frame,
        text="Сторона B",
        font=("Calibri", 16)
    )
    sideB_lbl.grid(row=6, column=1, pady=10)
    sideB_ent = Entry(
        frame
    )
    sideB_ent.grid(row=6, column=2)
    sideC_lbl = Label(
        frame,
        text="Сторона C",
        font=("Calibri", 16)
    )
    sideC_lbl.grid(row=7, column=1, pady=10)
    sideC_ent = Entry(
        frame
    )
    sideC_ent.grid(row=7, column=2)
    radius_lbl = Label(
        frame,
        text="Радиус вписанной окружности",
        font=("Calibri", 16)
    )
    radius_lbl.grid(row=8, column=1, pady=10)
    radius_ent = Entry(
        frame
    )
    radius_ent.grid(row=8, column=2)
    calc_btn = Button(
        frame,
        text="Рассчитать площадь",
        cursor="hand2",
        foreground="#006400",
        background="#00ff00",
        command=lambda: calc_treug_vpis_okr(sideA_ent.get(), sideB_ent.get(), sideC_ent.get(), radius_ent.get())
    )
    calc_btn.grid(row=9, column=2)
def calc_treug_vpis_okr(sideA, sideB, sideC, radius):
    sideA = float(sideA)
    sideB = float(sideB)
    sideC = float(sideC)
    radius = float(radius)
    poluperimetr = (sideA + sideB + sideC) / 2
    area = float(poluperimetr * radius)
    show_result(area)

def method_treugolnik_opis_okr():
    clear_extra_widgets()
    sideA_lbl = Label(
        frame,
        text="Сторона A",
        font=("Calibri", 16)
    )
    sideA_lbl.grid(row=5, column=1, pady=10)
    sideA_ent = Entry(
        frame
    )
    sideA_ent.grid(row=5, column=2)
    sideB_lbl = Label(
        frame,
        text="Сторона B",
        font=("Calibri", 16)
    )
    sideB_lbl.grid(row=6, column=1, pady=10)
    sideB_ent = Entry(
        frame
    )
    sideB_ent.grid(row=6, column=2)
    sideC_lbl = Label(
        frame,
        text="Сторона C",
        font=("Calibri", 16)
    )
    sideC_lbl.grid(row=7, column=1, pady=10)
    sideC_ent = Entry(
        frame
    )
    sideC_ent.grid(row=7, column=2)
    radius_lbl = Label(
        frame,
        text="Радиус описанной окружности",
        font=("Calibri", 16)
    )
    radius_lbl.grid(row=8, column=1, pady=10)
    radius_ent = Entry(
        frame
    )
    radius_ent.grid(row=8, column=2)
    calc_btn = Button(
        frame,
        text="Рассчитать площадь",
        cursor="hand2",
        foreground="#006400",
        background="#00ff00",
        command=lambda: calc_treug_opis_okr(sideA_ent.get(), sideB_ent.get(), sideC_ent.get(), radius_ent.get())
    )
    calc_btn.grid(row=9, column=2)
def calc_treug_opis_okr(sideA, sideB, sideC, radius):
    sideA = float(sideA)
    sideB = float(sideB)
    sideC = float(sideC)
    radius = float(radius)
    area = float(sideA * sideB * sideC / 4 / radius)
    show_result(area)

def figure_krug():
    clear_extra_widgets()
    methods = ["Через радиус"]
    method_combobox.config(values=methods, state="disabled")
    method_combobox.set("Через радиус")
    radius_lbl = Label(
        frame,
        text="Радиус",
        font=("Calibri", 16)
    )
    radius_lbl.grid(row=5, column=1, pady=10)
    radius_ent = Entry(
        frame
    )
    radius_ent.grid(row=5, column=2)
    calc_btn = Button(
        frame,
        text="Рассчитать площадь",
        cursor="hand2",
        foreground="#006400",
        background="#00ff00",
        command=lambda: calc_krug(radius_ent.get())
    )
    calc_btn.grid(row=6, column=2)
def calc_krug(radius):
    radius = float(radius)
    area = float(math.pi * radius**2)
    show_result(area)

def figure_sektor():
    clear_extra_widgets()
    methods = ["Через радиус и дугу"]
    method_combobox.config(values=methods, state="disabled")
    method_combobox.set("Через радиус и дугу")
    radius_lbl = Label(
        frame,
        text="Радиус",
        font=("Calibri", 16)
    )
    radius_lbl.grid(row=5, column=1, pady=10)
    radius_ent = Entry(
        frame
    )
    radius_ent.grid(row=5, column=2)
    duga_lbl = Label(
        frame,
        text="Дуга (в °)",
        font=("Calibri", 16)
    )
    duga_lbl.grid(row=6, column=1, pady=10)
    duga_ent = Entry(
        frame
    )
    duga_ent.grid(row=6, column=2)
    calc_btn = Button(
        frame,
        text="Рассчитать площадь",
        cursor="hand2",
        foreground="#006400",
        background="#00ff00",
        command=lambda: calc_sektor(radius_ent.get(), duga_ent.get())
    )
    calc_btn.grid(row=7, column=2)
def calc_sektor(radius, duga):
    radius = float(radius)
    duga = float(duga)
    area = float(math.pi * radius**2 * duga / 360)
    show_result(area)

def figure_4ugolnik():
    clear_extra_widgets()
    methods = ["Через диагонали и угол",
               "Через стороны (можно описать окружность)",
               "Через радиус вписанной окружности"]
    method_combobox.config(values=methods, state="readonly")
    method_combobox.set("Через диагонали и угол")
    method_combobox.bind("<<ComboboxSelected>>", selected_method_4ugolnik)
def selected_method_4ugolnik(event):
    selection = method_combobox.get()
    if selection == "Через диагонали и угол":
        method_4ugolnik_diagonali_ugol()
    elif selection == "Через стороны (можно описать окружность)":
        method_4ugolnik_storony()
    elif selection == "Через радиус вписанной окружности":
        method_4ugolnik_radius()

def method_4ugolnik_diagonali_ugol():
    clear_extra_widgets()
    diagonalA_lbl = Label(
        frame,
        text="Диагональ A",
        font=("Calibri", 16)
    )
    diagonalA_lbl.grid(row=5, column=1, pady=10)
    diagonalA_ent = Entry(
        frame
    )
    diagonalA_ent.grid(row=5, column=2)
    diagonalB_lbl = Label(
        frame,
        text="Диагональ B",
        font=("Calibri", 16)
    )
    diagonalB_lbl.grid(row=6, column=1, pady=10)
    diagonalB_ent = Entry(
        frame
    )
    diagonalB_ent.grid(row=6, column=2)
    angle_lbl = Label(
        frame,
        text="Угол между ними (в °)",
        font=("Calibri", 16)
    )
    angle_lbl.grid(row=7, column=1, pady=10)
    angle_ent = Entry(
        frame
    )
    angle_ent.grid(row=7, column=2)
    calc_btn = Button(
        frame,
        text="Рассчитать площадь",
        cursor="hand2",
        foreground="#006400",
        background="#00ff00",
        command=lambda: calc_treug_storony_ugol(diagonalA_ent.get(), diagonalB_ent.get(), angle_ent.get())
    )
    calc_btn.grid(row=8, column=2)

def method_4ugolnik_storony():
    clear_extra_widgets()
    sideA_lbl = Label(
        frame,
        text="Сторона A",
        font=("Calibri", 16)
    )
    sideA_lbl.grid(row=5, column=1, pady=10)
    sideA_ent = Entry(
        frame
    )
    sideA_ent.grid(row=5, column=2)
    sideB_lbl = Label(
        frame,
        text="Сторона B",
        font=("Calibri", 16)
    )
    sideB_lbl.grid(row=6, column=1, pady=10)
    sideB_ent = Entry(
        frame
    )
    sideB_ent.grid(row=6, column=2)
    sideC_lbl = Label(
        frame,
        text="Сторона C",
        font=("Calibri", 16)
    )
    sideC_lbl.grid(row=7, column=1, pady=10)
    sideC_ent = Entry(
        frame
    )
    sideC_ent.grid(row=7, column=2)
    sideD_lbl = Label(
        frame,
        text="Сторона D",
        font=("Calibri", 16)
    )
    sideD_lbl.grid(row=8, column=1, pady=10)
    sideD_ent = Entry(
        frame
    )
    sideD_ent.grid(row=8, column=2)
    calc_btn = Button(
        frame,
        text="Рассчитать площадь",
        cursor="hand2",
        foreground="#006400",
        background="#00ff00",
        command=lambda: calc_4ugolnik_storony(sideA_ent.get(), sideB_ent.get(), sideC_ent.get(), sideD_ent.get())
    )
    calc_btn.grid(row=9, column=2)
def calc_4ugolnik_storony(sideA, sideB, sideC, sideD):
    sideA = float(sideA)
    sideB = float(sideB)
    sideC = float(sideC)
    sideD = float(sideD)
    poluperimetr = (sideA + sideB + sideC + sideD) / 2
    area = float(math.sqrt((poluperimetr - sideA) * (poluperimetr - sideB) * (poluperimetr - sideC) * (poluperimetr - sideD)))
    show_result(area)

def method_4ugolnik_radius():
    clear_extra_widgets()
    sideA_lbl = Label(
        frame,
        text="Сторона A",
        font=("Calibri", 16)
    )
    sideA_lbl.grid(row=5, column=1, pady=10)
    sideA_ent = Entry(
        frame
    )
    sideA_ent.grid(row=5, column=2)
    sideB_lbl = Label(
        frame,
        text="Сторона B",
        font=("Calibri", 16)
    )
    sideB_lbl.grid(row=6, column=1, pady=10)
    sideB_ent = Entry(
        frame
    )
    sideB_ent.grid(row=6, column=2)
    sideC_lbl = Label(
        frame,
        text="Сторона C",
        font=("Calibri", 16)
    )
    sideC_lbl.grid(row=7, column=1, pady=10)
    sideC_ent = Entry(
        frame
    )
    sideC_ent.grid(row=7, column=2)
    sideD_lbl = Label(
        frame,
        text="Сторона D",
        font=("Calibri", 16)
    )
    sideD_lbl.grid(row=8, column=1, pady=10)
    sideD_ent = Entry(
        frame
    )
    sideD_ent.grid(row=8, column=2)
    radius_lbl = Label(
        frame,
        text="Радиус вписанной окружности",
        font=("Calibri", 16)
    )
    radius_lbl.grid(row=9, column=1, pady=10)
    radius_ent = Entry(
        frame
    )
    radius_ent.grid(row=9, column=2)
    calc_btn = Button(
        frame,
        text="Рассчитать площадь",
        cursor="hand2",
        foreground="#006400",
        background="#00ff00",
        command=lambda: calc_4ugolnik_radius(sideA_ent.get(), sideB_ent.get(), sideC_ent.get(), sideD_ent.get(), radius_ent.get())
    )
    calc_btn.grid(row=10, column=2)
def calc_4ugolnik_radius(sideA, sideB, sideC, sideD, radius):
    sideA = float(sideA)
    sideB = float(sideB)
    sideC = float(sideC)
    sideD = float(sideD)
    radius = float(radius)
    poluperimetr = (sideA + sideB + sideC + sideD) / 2
    area = float(poluperimetr * radius)
    show_result(area)

def convert_degrees_to_radians(alpha):
    return math.pi / 180 * alpha
def show_result(area):
    area = round(area, 2)
    messagebox.showinfo('Результат', f'Площадь равна {area}.')


frame = Frame(
   window,
   padx = 10,
   pady = 10
)
frame.pack(expand=True)

figure_lbl = Label(
   frame,
   text="Выберите фигуру",
    font=("Calibri", 16)
)
figure_lbl.grid(row=1, column=1)

figures = ["Параллелограмм",
           "Прямоугольник",
           "Квадрат",
           "Ромб",
           "Трапеция",
           "Треугольник",
           "Круг",
           "Сектор",
           "Четырёхугольник"]
combobox = Combobox(frame, values=figures, width=30, state="readonly")
combobox.grid(row=2, column=1)
combobox.set("Параллелограмм")
combobox.bind("<<ComboboxSelected>>", selected)

method_lbl = Label(
        frame,
        text="Выберите метод",
        font=("Calibri", 16)
    )
method_lbl.grid(row=3, column=1)

method_combobox = Combobox(frame, width=45, state="readonly")
method_combobox.grid(row=4, column=1)

global_widgets = frame.winfo_children()

def clear_extra_widgets():
    for widget in frame.winfo_children():
        if widget not in global_widgets:
            widget.destroy()

window.mainloop()
