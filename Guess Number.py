import  random
while True:
    min_num = 0
    max_num = 0
    random_number = 0
    win = False
    count = 0

    print("")
    print("Добро пожаловать в игру \"Угадай число\"!")
    print("Укажите диапозон, в котором программа загадает число.")
    try:
        min_num = int(input("Введите первое число: "))
        max_num = int(input("Введите первое число: "))
    except:
        print("Что-то пошло не так. Возможно вы ввели некорректные числа. Присвоен стандартный диапозон: от 1 до 10.")
        min_num = 1
        max_num = 10

    random_number = 0
    try:
        random_number = random.randint(min_num, max_num)
    except:
        random_number = random.randint(max_num, min_num)

    print("")
    print("Программа загадала число.")

    while win == False:
        print("")
        number = 0
        try:
            number = int(input("Введите число: "))
        except:
            number = 0
        if number > random_number:
            print("Загаданное число меньше.")
        elif number < random_number:
            print("Загаданное число больше.")
        elif number == random_number:
            win = True
        count += 1
    print("")
    print(f"Поздравляем! Вы угадали! Это действительно число {random_number}!")
    print(f"Вы угадали с {count} попытки.")
    print("")
    input("Нажмите Enter для выхода.")