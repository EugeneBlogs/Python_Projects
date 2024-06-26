'''
Для красивого отображения интерфейса используется библиотека "Rich".
Чтобы ёё установить, напишите в командной строке команду "pip install rich".

Если командная строка выдаёт ошибку, сделайте следующие действия:
1. Откройте "Изменение системных переменных среды".
2. Откройте "Переменные среды".
3. Выберите "Path" и нажмите "Изменить".
4. Создайте 2 ссылки: "C:/Users/mylni/AppData/Local/Programs/Python/Python312" и "C:/Users/mylni/AppData/Local/Programs/Python/Python312/Scripts" (ссылки немного могут отличаться).
'''

from rich import print
from rich.prompt import Prompt
from rich.console import Console
from rich.table import Table
import random
from time import sleep
from rich.progress import track

def do_step(step):
    sleep(random.uniform(0.001, 0.03))

def plus_massa(weight, height):
    cool = False
    error = False
    weight = round(weight, 1)
    cool_weight = weight
    while cool == False:
        cool_weight += 0.1
        BMI = cool_weight / (height ** 2)
        if 18.5 < BMI <= 25:
            cool = True
        elif BMI < 0:
            cool = True
            error = True
    if error:
        print(":exclamation_mark: [bold underline red]Что-то пошло не так. Возможно, вы ввели некорректные числа.[/bold underline red] :exclamation_mark:")
    elif cool:
        difference = cool_weight - weight
        difference = round(difference, 1)
        print(f"[underline green]До нормы[/underline green] нужно набрать {difference} кг, чтобы вес стал {cool_weight}.")

def minus_massa(weight, height):
    cool = False
    error = False
    weight = round(weight, 1)
    cool_weight = weight
    while cool == False:
        cool_weight -= 0.1
        BMI = cool_weight / (height ** 2)
        if 18.5 < BMI <= 25:
            cool = True
        elif BMI < 0:
            cool = True
            error = True
    if error:
        print(":exclamation_mark: [bold underline red]Что-то пошло не так. Возможно, вы ввели некорректные числа.[/bold underline red] :exclamation_mark:")
    elif cool:
        difference = weight - cool_weight
        difference = round(difference, 1)
        print(f"[underline green]До нормы[/underline green] нужно скинуть {difference} кг, чтобы вес стал {cool_weight}.")

while True:
    print("")
    print("Добро пожаловать в [bold magenta blink]\"Калькулятор ИМТ\"[/bold magenta blink]! :pizza:")
    print("[italic yellow]Что делаем?[/italic yellow]")
    print("Рассчитать ИМТ - 1")
    print("Категории ИМТ - 2")
    choose = 1
    try:
        choose = int(input("Выбор: "))
    except:
        choose = 1
    if choose == 1:
        print("")
        weight = Prompt.ask("Ваш вес (кг)", default="63.4")
        height = Prompt.ask("Ваш рост (см)", default="176")
        if float(weight) <= 0 or float(height) <= 0:
            print(":exclamation_mark: [bold underline red]Числа должны быть положительные.[/bold underline red] :exclamation_mark:")
        else:
            try:
                weight = float(weight)
                height = float(height)
                height = height / 100
                BMI = weight/(height**2)
                BMI = round(BMI, 1)
                for step in track(range(100), description="Вычисляем ..."):
                    do_step(step)
                print("")
                print(f"[magenta]Ваш ИМТ:[/magenta] {BMI}.")
                if BMI < 16:
                    print("У вас [blue]выраженный дефицит массы[/blue].")
                    plus_massa(weight, height)
                elif 16 <= BMI <= 18.5:
                    print("У вас [cyan]недостаточная масса[/cyan].")
                    plus_massa(weight, height)
                elif 18.5 < BMI <= 25:
                    print("У вас [green]норма[/green].")
                elif 25 < BMI <= 30:
                    print("У вас [dark_green]избыточная масса (предожирение)[/dark_green].")
                    minus_massa(weight, height)
                elif 30 < BMI <= 35:
                    print("У вас [yellow]ожирение 1 степени[/yellow].")
                    minus_massa(weight, height)
                elif 35 < BMI <= 40:
                    print("У вас [red]ожирение 2 степени[/red].")
                    minus_massa(weight, height)
                elif BMI > 40:
                    print("У вас [dark_red]ожирение 3 степени[/dark_red].")
                    minus_massa(weight, height)
            except:
                print(":exclamation_mark: [bold underline red]Что-то пошло не так. Возможно, вы ввели некорректные числа.[/bold underline red] :exclamation_mark:")
    elif choose == 2:
        print("")
        print("[underline blue]ИМТ[/underline blue] - индекс массы тела")
        print("[underline blue]Формула[/underline blue] - масса/рост в квадрате")
        print("[underline blue]Единицы измерения[/underline blue] - кг/м²")
        print("")

        table = Table(title="Интерпретация показателей ИМТ")

        table.add_column("ИМТ", justify="right", style="green", no_wrap=True)
        table.add_column("Значение", justify="center", style="red")

        table.add_row("16 и менее", "Выраженный дефицит массы")
        table.add_row("16-18,5", "Недостаточная масса")
        table.add_row("18,5-25", "Норма")
        table.add_row("25-30", "Избыточная масса (предожирение)")
        table.add_row("30-35", "Ожирение 1 степени")
        table.add_row("35-40", "Ожирение 2 степени")
        table.add_row("40 и более", "Ожирение 3 степени")

        console = Console()
        console.print(table)
    print("")
    print("[italic green]Нажмите [underline red]Enter[/underline red] для перезапуска.[/italic green]")
    input()
