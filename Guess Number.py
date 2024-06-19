'''
Для красивого отображения интерфейса используется библиотека "Rich".
Чтобы ёё установить, напишите в командной строке команду "pip install rich".

Если командная строка выдаёт ошибку, сделайте следующие действия:
1. Откройте "Изменение системных переменных среды".
2. Откройте "Переменные среды".
3. Выберите "Path" и нажмите "Изменить".
4. Создайте 2 ссылки: "C:/Users/mylni/AppData/Local/Programs/Python/Python312" и "C:/Users/mylni/AppData/Local/Programs/Python/Python312/Scripts" (ссылки немного могут отличаться).
'''

import random
from rich import print

while True:
    min_num = 0
    max_num = 0
    random_number = 0
    win = False
    count = 0

    print("")
    print("Добро пожаловать в игру [bold yellow on red blink]\"Угадай число\"[/bold yellow on red blink]! :face_with_monocle:")
    print("Укажите [italic blue]диапозон[/italic blue], в котором программа загадает число.")
    try:
        min_num = int(input("Введите первое число: "))
        max_num = int(input("Введите первое число: "))
    except:
        print(":exclamation_mark: [bold red]Что-то пошло не так. Возможно, вы ввели некорректные числа. Присвоен стандартный диапозон: [underline yellow]от 1 до 10[/underline yellow].[/bold red] :exclamation_mark:")
        min_num = 1
        max_num = 10

    random_number = 0
    try:
        random_number = random.randint(min_num, max_num)
    except:
        random_number = random.randint(max_num, min_num)

    print("")
    print(":ok_hand: [bold green]Программа загадала число.[/bold green] :ok_hand:")

    while win == False:
        print("")
        number = 0
        try:
            number = int(input("Введите число: "))
        except:
            number = 0
        if number > random_number:
            print(":down_arrow: [italic cyan]Загаданное число меньше.[/italic cyan] :down_arrow:")
        elif number < random_number:
            print(":up_arrow: [italic cyan]Загаданное число больше.[/italic cyan] :up_arrow:")
        elif number == random_number:
            win = True
        count += 1
    print("")
    print(f"[bold red on yellow blink]Поздравляем! Вы угадали![bold red on yellow blink] Это действительно число {random_number}!")
    print(f"Вы угадали с {count} попытки.")
    print("")
    print("[italic green]Нажмите [underline red]Enter[/underline red] для перезапуска.[/italic green]")
    input()
