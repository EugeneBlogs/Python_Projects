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
                print(field[i][j], end=' ')
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
                field[2][0] == field[2][1] == field[2][2] != "-") or (field[0][0] == field[1][0] == field[2][0] != "-") or (
                field[0][1] == field[1][1] == field[2][1] != "-") or (field[0][2] == field[1][2] == field[2][2] != "-") or (
                field[0][0] == field[1][1] == field[2][2] != "-") or (field[2][0] == field[1][1] == field[0][2] != "-"):
            win = True
            if player == "X":
                winner = "O"
            elif player == "O":
                winner = "X"

    def ChechNobody():
        global nobody
        if field[0][0] != "-" and field[0][1] != "-" and field[0][2] != "-" and field[1][0] != "-" and field[1][1] != "-" and field[1][2] != "-" and field[2][0] != "-" and field[2][1] != "-" and field[2][2] != "-":
            nobody = True

    print("")
    print("Добро пожаловать в игру \"Крестики-Нолики\"!")
    print("Чтобы указать нужную ячейку, введите 2 числа через пробел в формате РЯД СТОЛБЕЦ (например: 2 3, где 2 - ряд, а 3 - столбец).")
    print("Как играем?")
    print("2 человека - 1")
    print("Человек против Компьютера - 2")
    choose = 1
    try:
        choose = int(input("Выбор: "))
    except:
        choose = 1

    if choose == 1:
        print("")
        print("2 человека")
        print("")
        while win == False and nobody == False:
            Draw()
            try:
                row, column = map(int, input(f"Ход игрока {player}: ").split())
                if field[row-1][column-1] == "-":
                    field[row-1][column-1] = player
                    Change()
                    CheckWinner()
                    ChechNobody()
                else:
                    print("Ячейка занята.")
            except:
                print("Что-то пошло не так. Возможно вы ввели некорректные числа.")
    if choose == 2:
        print("")
        print("Человек - X Компьютер - O")
        print("")
        player_row = 0
        player_column = 0
        while win == False and nobody == False:
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
                        if win == False and nobody == False:
                            print("")
                            print("Компьютер делает ход ...")
                            time.sleep(1)
                    else:
                        print("Ячейка занята.")
                except:
                    print("Что-то пошло не так. Возможно вы ввели некорректные числа.")
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
                    if hod == False:
                        row, column = map(int, variants[i].split())
                        if field[row][column] == "-":
                            field[row][column] = player
                            hod = True
                            Change()
                            CheckWinner()
                            ChechNobody()
                if hod == False:
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
        print(f"Выиграли {winner}!")
    elif nobody:
        print("Ничья!")
    print("")
    input("Нажмите Enter для перезапуска.")