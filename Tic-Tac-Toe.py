'''
Для красивого отображения интерфейса используется библиотека "Rich".
Чтобы ёё установить, напишите в командной строке команду "pip install rich".

Если командная строка выдаёт ошибку, сделайте следующие действия:
1. Откройте "Изменение системных переменных среды".
2. Откройте "Переменные среды".
3. Выберите "Path" и нажмите "Изменить".
4. Создайте 2 ссылки: "C:/Users/mylni/AppData/Local/Programs/Python/Python312"
и "C:/Users/mylni/AppData/Local/Programs/Python/Python312/Scripts" (ссылки немного могут отличаться).
'''

from rich import print
from rich.console import Console

console = Console()

while True:
    field = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
    win = False
    nobody = False
    player = "X"
    winner = "X"

    import random
    import time


    def Draw():
        print()
        for i in range(0, len(field)):
            for j in range(0, len(field[i])):
                if field[i][j] == "X":
                    print("[red]X[/red]", end=' ')
                elif field[i][j] == "O":
                    print("[blue]O[/blue]", end=' ')
                else:
                    print("[green]-[/green]", end=' ')
            print()


    def Change():
        global player
        if player == "X":
            player = "O"
        elif player == "O":
            player = "X"


    def CheckWinner():
        global win
        global winner
        if (field[0][0] == field[0][1] == field[0][2] != "-") or (field[1][0] == field[1][1] == field[1][2] != "-") or (
                field[2][0] == field[2][1] == field[2][2] != "-") or (
                field[0][0] == field[1][0] == field[2][0] != "-") or (
                field[0][1] == field[1][1] == field[2][1] != "-") or (
                field[0][2] == field[1][2] == field[2][2] != "-") or (
                field[0][0] == field[1][1] == field[2][2] != "-") or (field[2][0] == field[1][1] == field[0][2] != "-"):
            win = True
            if player == "X":
                winner = "O"
            elif player == "O":
                winner = "X"


    def ChechNobody():
        global nobody
        if (field[0][0] != "-" and field[0][1] != "-" and field[0][2] != "-" and field[1][0] != "-"
                and field[1][1] != "-" and field[1][2] != "-" and field[2][0] != "-" and field[2][1] != "-"
                and field[2][2] != "-"):
            nobody = True


    print("")
    print("Добро пожаловать в игру [bold yellow on red blink]\"Крестики-Нолики\"[/bold yellow on red blink]! "
          ":waving_hand:")
    print("Чтобы указать нужную ячейку, введите [underline blue]2 числа через пробел[/underline blue] "
          "в формате РЯД СТОЛБЕЦ (например: 2 3, где 2 - ряд, а 3 - столбец).")
    print("[italic green]Как играем?[/italic green]")
    print("2 человека - 1")
    print("Человек против Компьютера - 2")
    choose = 1
    try:
        choose = int(input("Выбор: "))
    except:
        choose = 1

    if choose == 1:
        print("")
        print("[bold green on blue blink]2 человека[/bold green on blue blink]")
        print("")
        while not win and not nobody:
            Draw()
            try:
                row, column = map(int, input(f"Ход игрока {player}: ").split())
                if field[row - 1][column - 1] == "-":
                    field[row - 1][column - 1] = player
                    Change()
                    CheckWinner()
                    ChechNobody()
                else:
                    print(":warning:  [underline yellow]Ячейка занята.[/underline yellow] :warning:")
            except:
                print(":exclamation_mark: [bold underline red]Что-то пошло не так. "
                      "Возможно, вы ввели некорректные числа.[/bold underline red] :exclamation_mark:")
    if choose == 2:
        print("")
        print("[bold green on blue blink]Человек - [red]X[/red] "
              "Компьютер - [yellow]O[/yellow][/bold green on blue blink]")
        print("")
        player_row = 0
        player_column = 0
        while not win and not nobody:
            Draw()
            if player == "X":
                try:
                    row, column = map(int, input(f"Ход игрока {player}: ").split())
                    if field[row - 1][column - 1] == "-":
                        field[row - 1][column - 1] = player
                        player_row = row - 1
                        player_column = column - 1
                        Change()
                        CheckWinner()
                        ChechNobody()
                        if not win and not nobody:
                            with console.status("[bold cyan]Компьютер делает ход ...[/bold cyan]") as status:
                                for i in range(3):
                                    time.sleep(1)
                    else:
                        print(":warning:  [underline yellow]Ячейка занята.[/underline yellow] :warning:")
                except:
                    print(":exclamation_mark: [bold underline red]Что-то пошло не так. "
                          "Возможно, вы ввели некорректные числа.[/bold underline red] :exclamation_mark:")
            elif player == "O":
                variants = []
                if field[0][0] == field[0][1] == "O" and field[0][2] == "-":
                    variants.append("0 2")
                elif field[0][0] == field[0][2] == "O" and field[0][1] == "-":
                    variants.append("0 1")
                elif field[0][1] == field[0][2] == "O" and field[0][0] == "-":
                    variants.append("0 0")
                elif field[1][0] == field[1][1] == "O" and field[1][2] == "-":
                    variants.append("1 2")
                elif field[1][0] == field[1][2] == "O" and field[1][1] == "-":
                    variants.append("1 1")
                elif field[1][1] == field[1][2] == "O" and field[1][0] == "-":
                    variants.append("1 0")
                elif field[2][0] == field[2][1] == "O" and field[2][2] == "-":
                    variants.append("2 2")
                elif field[2][0] == field[2][2] == "O" and field[2][1] == "-":
                    variants.append("2 1")
                elif field[2][1] == field[2][2] == "O" and field[2][0] == "-":
                    variants.append("2 0")
                elif field[0][0] == field[1][0] == "O" and field[2][0] == "-":
                    variants.append("2 0")
                elif field[0][0] == field[2][0] == "O" and field[1][0] == "-":
                    variants.append("1 0")
                elif field[1][0] == field[2][0] == "O" and field[0][0] == "-":
                    variants.append("0 0")
                elif field[0][1] == field[1][1] == "O" and field[2][1] == "-":
                    variants.append("2 1")
                elif field[0][1] == field[2][1] == "O" and field[1][1] == "-":
                    variants.append("1 1")
                elif field[1][1] == field[2][1] == "O" and field[0][1] == "-":
                    variants.append("0 1")
                elif field[0][2] == field[1][2] == "O" and field[2][2] == "-":
                    variants.append("2 2")
                elif field[0][2] == field[2][2] == "O" and field[1][2] == "-":
                    variants.append("1 2")
                elif field[1][2] == field[2][2] == "O" and field[0][2] == "-":
                    variants.append("0 2")
                elif field[0][0] == field[1][1] == "O" and field[2][2] == "-":
                    variants.append("2 2")
                elif field[0][0] == field[2][2] == "O" and field[1][1] == "-":
                    variants.append("1 1")
                elif field[1][1] == field[2][2] == "O" and field[0][0] == "-":
                    variants.append("0 0")
                elif field[2][0] == field[1][1] == "O" and field[0][2] == "-":
                    variants.append("0 2")
                elif field[2][0] == field[0][2] == "O" and field[1][1] == "-":
                    variants.append("1 1")
                elif field[1][1] == field[0][2] == "O" and field[2][0] == "-":
                    variants.append("2 0")
                elif field[0][0] == field[0][1] == "X" and field[0][2] == "-":
                    variants.append("0 2")
                elif field[0][0] == field[0][2] == "X" and field[0][1] == "-":
                    variants.append("0 1")
                elif field[0][1] == field[0][2] == "X" and field[0][0] == "-":
                    variants.append("0 0")
                elif field[1][0] == field[1][1] == "X" and field[1][2] == "-":
                    variants.append("1 2")
                elif field[1][0] == field[1][2] == "X" and field[1][1] == "-":
                    variants.append("1 1")
                elif field[1][1] == field[1][2] == "X" and field[1][0] == "-":
                    variants.append("1 0")
                elif field[2][0] == field[2][1] == "X" and field[2][2] == "-":
                    variants.append("2 2")
                elif field[2][0] == field[2][2] == "X" and field[2][1] == "-":
                    variants.append("2 1")
                elif field[2][1] == field[2][2] == "X" and field[2][0] == "-":
                    variants.append("2 0")
                elif field[0][0] == field[1][0] == "X" and field[2][0] == "-":
                    variants.append("2 0")
                elif field[0][0] == field[2][0] == "X" and field[1][0] == "-":
                    variants.append("1 0")
                elif field[1][0] == field[2][0] == "X" and field[0][0] == "-":
                    variants.append("0 0")
                elif field[0][1] == field[1][1] == "X" and field[2][1] == "-":
                    variants.append("2 1")
                elif field[0][1] == field[2][1] == "X" and field[1][1] == "-":
                    variants.append("1 1")
                elif field[1][1] == field[2][1] == "X" and field[0][1] == "-":
                    variants.append("0 1")
                elif field[0][2] == field[1][2] == "X" and field[2][2] == "-":
                    variants.append("2 2")
                elif field[0][2] == field[2][2] == "X" and field[1][2] == "-":
                    variants.append("1 2")
                elif field[1][2] == field[2][2] == "X" and field[0][2] == "-":
                    variants.append("0 2")
                elif field[0][0] == field[1][1] == "X" and field[2][2] == "-":
                    variants.append("2 2")
                elif field[0][0] == field[2][2] == "X" and field[1][1] == "-":
                    variants.append("1 1")
                elif field[1][1] == field[2][2] == "X" and field[0][0] == "-":
                    variants.append("0 0")
                elif field[2][0] == field[1][1] == "X" and field[0][2] == "-":
                    variants.append("0 2")
                elif field[2][0] == field[0][2] == "X" and field[1][1] == "-":
                    variants.append("1 1")
                elif field[1][1] == field[0][2] == "X" and field[2][0] == "-":
                    variants.append("2 0")
                else:
                    if player_row == 0 and player_column == 0:
                        variants.append("0 1")
                        variants.append("0 2")
                        variants.append("1 1")
                        variants.append("2 2")
                        variants.append("1 0")
                        variants.append("2 0")
                    elif player_row == 0 and player_column == 1:
                        variants.append("0 0")
                        variants.append("0 2")
                        variants.append("1 1")
                        variants.append("2 1")
                    elif player_row == 0 and player_column == 2:
                        variants.append("0 0")
                        variants.append("0 1")
                        variants.append("1 1")
                        variants.append("2 0")
                        variants.append("1 2")
                        variants.append("2 2")
                    elif player_row == 1 and player_column == 0:
                        variants.append("0 0")
                        variants.append("2 0")
                        variants.append("1 1")
                        variants.append("1 2")
                    elif player_row == 1 and player_column == 1:
                        variants.append("0 0")
                        variants.append("0 1")
                        variants.append("0 2")
                        variants.append("1 0")
                        variants.append("1 2")
                        variants.append("2 0")
                        variants.append("2 1")
                        variants.append("2 2")
                    elif player_row == 1 and player_column == 2:
                        variants.append("0 2")
                        variants.append("2 2")
                        variants.append("1 0")
                        variants.append("1 1")
                    elif player_row == 2 and player_column == 0:
                        variants.append("0 0")
                        variants.append("1 0")
                        variants.append("1 1")
                        variants.append("0 2")
                        variants.append("2 1")
                        variants.append("2 2")
                    elif player_row == 2 and player_column == 1:
                        variants.append("2 0")
                        variants.append("2 2")
                        variants.append("0 1")
                        variants.append("1 1")
                    elif player_row == 2 and player_column == 2:
                        variants.append("0 2")
                        variants.append("1 2")
                        variants.append("0 0")
                        variants.append("1 1")
                        variants.append("2 0")
                        variants.append("2 1")
                random.shuffle(variants)
                hod = False
                for i in range(len(variants)):
                    if not hod:
                        row, column = map(int, variants[i].split())
                        if field[row][column] == "-":
                            field[row][column] = player
                            hod = True
                            Change()
                            CheckWinner()
                            ChechNobody()
                if not hod:
                    rand_row = random.randint(1, 3)
                    rand_column = random.randint(1, 3)
                    if field[rand_row - 1][rand_column - 1] == "-":
                        field[rand_row - 1][rand_column - 1] = player
                        Change()
                        CheckWinner()
                        ChechNobody()
    Draw()
    print("")
    if win:
        if winner == "X":
            print(f"[bold yellow blink]Выиграли[/bold yellow blink] [red]X[/red]!")
        elif winner == "O":
            print(f"[bold yellow blink]Выиграли[/bold yellow blink] [blue]O[/blue]!")
    elif nobody:
        print("[bold cyan blink]Ничья![/bold cyan blink]")
    print("")
    print("[italic green]Нажмите [underline red]Enter[/underline red] для перезапуска.[/italic green]")
    str_text = input()
    if str_text == "RPS" or str_text == "КМН":
        print("")
        print("[bold yellow blink]Поздравляем![/bold yellow blink] Вы обнаружили пасхалку! :clap:")
        print("Давайте сыргаем в игру [italic red]\"Камень, Ножницы, Бумага\"[/italic red]!")
        print("[underline green]Что выбираете?[/underline green]")
        print("Камень - К")
        print("Ножницы - Н")
        print("Бумага - Б")
        choose_object = input("Выбор: ")
        variants = ["К", "Н", "Б", "к", "н", "б"]
        while choose_object not in variants:
            print("")
            print(":exclamation_mark: [bold underline red]Такого предмета нет. "
                  "Повторите попытку.[/bold underline red] :exclamation_mark:")
            choose_object = input("Выбор: ")
        user = ""
        if choose_object == "К" or choose_object == "к":
            user = "Камень"
        elif choose_object == "Н" or choose_object == "н":
            user = "Ножницы"
        elif choose_object == "Б" or choose_object == "б":
            user = "Бумага"
        rnd = random.randint(1, 3)
        computer = ""
        if rnd == 1:
            computer = "Камень"
        elif rnd == 2:
            computer = "Ножницы"
        elif rnd == 3:
            computer = "Бумага"
        print("")
        print(f"[red]Вы[/red]: {user}.")
        print(f"[yellow]Компьютер[/yellow]: {computer}.")
        if user == computer:
            print("[bold green blink]Ничья![/bold green blink]")
        elif user == "Камень" and computer == "Ножницы":
            print("[bold yellow blink]Вы выиграли![/bold yellow blink]")
        elif user == "Камень" and computer == "Бумага":
            print("[bold red blink]Компьютер выиграл![/bold red blink]")
        elif user == "Ножницы" and computer == "Камень":
            print("[bold red blink]Компьютер выиграл![/bold red blink]")
        elif user == "Ножницы" and computer == "Бумага":
            print("[bold yellow blink]Вы выиграли![/bold yellow blink]")
        elif user == "Бумага" and computer == "Камень":
            print("[bold yellow blink]Вы выиграли![/bold yellow blink]")
        elif user == "Бумага" and computer == "Ножницы":
            print("[bold red blink]Компьютер выиграл![/bold red blink]")
