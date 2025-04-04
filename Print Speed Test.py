import random
import time
from datetime import date, datetime
from tkinter import *
from tkinter import messagebox, simpledialog
from tkinter.messagebox import askyesno, showwarning, showerror

print("!!!")
print("В консоль будут выводится отчёты об ошибках. Чтобы консоль не открывалась - сохраните файл в формате '.pyw'.")
print("!!!")

current_text = ""
mistakes = 0
start_time = None
end_time = None
stop_test = False

variants = [
    "Школа - это место, где мы не просто учимся, а формируем будущее. Здесь мы получаем знания, дружим, открываем для себя мир науки и искусства. Учитель - наш проводник в этом путешествии, помогая нам стать умнее и лучше. Каждый школьный день наполнен открытиями и возможностями. Школа - это не просто учебное заведение, это наша вторая семья, где мы растём и совершаем первые шаги к своей мечте.",
    "Компьютерные технологии сегодня стали неотъемлемой частью нашей повседневной жизни. Программирование, интернет, социальные сети - всё это неотъемлемые компоненты современного мира. С каждым днём технические новшества становятся доступнее и более удобными для использования. Открывайте новые горизонты с помощью высокотехнологичных устройств и приложений. Будущее уже здесь, и оно ассоциируется с миром компьютерных технологий.",
    "Лиса и медведь жили в одном лесу. Лиса была хитрой и ловкой, а медведь - сильным и могучим. Они часто ссорились из-за территории и еды. Но однажды, когда заснежило, лиса и медведь решили объединиться, чтобы найти убежище и еду. Они стали неразлучными друзьями, помогая друг другу выжить в лютом холоде. Опасности поджидали их на каждом шагу, но благодаря силе дружбы и уму лисы они преодолели все трудности вместе.",
    "Дружба - это особенное чувство, которое объединяет людей и делает их жизнь ярче и насыщеннее. Верные друзья всегда поддержат в трудную минуту, поделятся радостью и успехами. Они готовы пройти сквозь огонь и воду, лишь бы помочь друг другу. Настоящая дружба не знает зависти и обмана, в ней ценится искренность и преданность. Друзья - это необходимость, которая делает нашу жизнь более значимой и запоминающейся.",
    "Детство - это время волшебства, игр и открытий. Каждый день наполненный новыми приключениями и радостью. В детстве мы строим замки из песка на пляже, ловим бабочек в саду и делаем первые шаги в мире знаний. Вспоминая свои детские годы, мы вспоминаем беззаботное счастье и тепло родительской любви. Сколько воспоминаний и смеха умещается в одном детском сердце!",
    "Зима пришла с белыми сугробами и заморозками. Морозное утро, сверкающий иней на ветвях, дети катаются на санках и строят снеговиков. Воздух прозрачный, в нём чувствуется свежесть и чистота зимнего утра. Хрустальные снежинки падают с небес, придавая пейзажу сказочный вид. Скоро наступит время катания на коньках и снежных баталий. Зима - время волшебства и радости!",
    "Лето - это время ярких красок и тёплого солнца. Зелёные листья шелестят на ветру, цветы расцветают во всей своей красе. Воздух наполнен запахом свежей травы и спелых фруктов. Дети веселятся на пляже, строят замки из песка и купаются в море. Каждый день приносит новые впечатления и радостные моменты. Лето - пора безмятежности и свободы.",
    "Счастье - это тёплое чувство, которое наполняет сердце радостью и улыбкой. Оно может быть скрыто в мелочах: луч солнца на лице, улыбка незнакомца, тёплый чай в холодный день. Счастлив тот, кто умеет видеть эту красоту в повседневных моментах. Счастье - это осознание прекрасного вокруг, способность радоваться жизни и ценить каждый миг. Найдите своё счастье в мелочах и делитесь им с другими.",
    "Юмор - это как волшебное зелье, способное рассеять тучи серости и наполнить жизнь яркими красками. Умение видеть вещи с юмором делает нас сильнее и открытее к миру. Смех объединяет людей, делает нас ближе и дарит радость. Зачастую, именно в трудных ситуациях, юмор помогает нам сохранить душевное равновесие. Позвольте смеху стать вашим проводником через жизнь, и вы увидите, как мир станет ярче и веселее!",
    "Мечта - это капля дождя на облаках летнего неба, сверкающая звезда в море тёмной ночи. Она живёт внутри нас, подстёгивает к действиям, вдохновляет на подвиги. Мечта - это маяк на морском берегу, указывающий путь к счастью и самосовершенствованию. Каждый из нас носит в себе свою уникальную мечту, достигнуть которой поможет вера, упорство и работа. Пускай мечта будет вашим компасом в жизни, направляющим к светлому будущему.",
    "Чтение является одним из самых полезных источников для расширения кругозора и интеллектуального развития. Это способствует развитию логического мышления, улучшению памяти и концентрации внимания. Чтение также помогает улучшить навыки общения и расширить словарный запас. Кроме того, книги иногда могут послужить вдохновением для саморазвития и поиска новых целей в жизни. Поэтому постарайтесь уделить время чтению каждый день - это будет полезным для вашего умственного и духовного развития.",
    "Москва - культурный, исторический и политический центр России. Это город с величественной архитектурой, богатой историей и миллионным населением. Москва известна своими достопримечательностями, такими как Красная площадь, Кремль, Большой театр. Здесь находятся правительственные органы, важные культурные центры и деловые кварталы. Москва - символ мощи и величия России, место, где переплетаются история и современность.",
    "Красота играет важную роль в жизни человека. Красота присутствует в природе, искусстве, в мелочах повседневной жизни. Красота - это не только внешний облик, но и внутренняя гармония, любовь, доброта. Красота важна для каждого человека, поскольку она способна поднимать настроение, укреплять внутреннюю силу и вдохновлять на свершения. Созерцание красоты позволяет забыть о повседневных заботах и насладиться моментом. Она наполняет нас позитивом, помогает видеть прекрасное даже в самых трудных ситуациях.",
    "Космос - это бескрайнее пространство, в котором скрыты многочисленные тайны. Звёзды, планеты, галактики складываются в великолепные картины бесконечной вселенной. Исследования космоса открывают перед нами новые горизонты и заставляют удивляться величию космической мудрости. Звёзды светят как знаки тайны и красоты, вдохновляя нас стремиться за грань возможностей и познания. Космос - это величественное воплощение силы и гармонии, вызывающее бесконечное восхищение и любопытство.",
    "Семья - это тепло и уют, в котором каждый находит понимание, поддержку и любовь. Вместе мы смеёмся и плачем, растём и учимся. Семейные ценности объединяют нас, делая нашу жизнь яркой и значимой. В семье ценится каждый член и каждое мгновение вместе. Отношения внутри семьи формируют наше мировоззрение и определяют наше благополучие. Семья - это опора и радость, которые сопровождают нас на всём жизненном пути."]


def change(event):
    global start_time
    global end_time
    global stop_test
    global current_text
    global mistakes

    text_lbl.config(text=current_text)

    text = event.widget.get("1.0", "end")
    text = text.replace("\n", "")

    percent = int(len(text) / len(current_text) * 100)
    window.title(f"Написано: {percent}%")

    symbols_original = []
    symbols_user = []
    for symbol in current_text:
        symbols_original += symbol
    for symbol in text:
        symbols_user += symbol

    for i in range(len(symbols_user)):
        if symbols_user[i] != symbols_original[i]:
            mistakes -= 1
            replace_text = ""
            symbols_original[i] = f"!{symbols_original[i]}!"
            for symbol in range(len(symbols_original)):
                replace_text += symbols_original[symbol]
            text_lbl.config(text=replace_text)

    if text == f"{current_text}" and stop_test == False:
        stop_test = True
        textbox.config(state="disabled")

        end_time = time.time()
        time_lapsed = end_time - start_time

        speed = int(len(current_text) / int(time_lapsed))
        WPM = int(int(len(current_text) / 5) / int(int(time_lapsed) / 60))
        accuracy = int(mistakes / len(current_text) * 100)
        if accuracy < 0:
            accuracy = 0

        messagebox.showinfo('Результат',
                            f'Информация о тексте:\nСимволы: {len(current_text)}.\nСлова: {len(current_text.split(" "))}.\n\nИнформация о тесте:\nВремя: {time_convert(time_lapsed)}.\nСкорость: {speed} символов/секунду.\nWPM (словом считается каждые 5 символов): {WPM} слов/минуту.\nТочность: {accuracy}%.')
        if askyesno(title="Сохранение", message="Сохранить данный результат в историю?"):
            root = Tk()
            root.withdraw()
            name = simpledialog.askstring(title="Имя", prompt="Как Вас зовут?")
            try:
                text_file = open('./files/History.txt', 'r', encoding='utf-8').read()
                if text_file == None or text_file == "":
                    print("Yes")
                    text_file = ""
                file = open('./files/History.txt', 'w', encoding='utf-8')
                text_add = f"{name} ({date.today().day}.{date.today().month}.{date.today().year} {datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}) - Текст: '{current_text.split(" ")[0]}'. Время: {time_convert(time_lapsed)}. Скорость: {speed} символов/секунду. WPM: {WPM} слов/минуту. Точность: {accuracy}%."
                result = f"{text_file}\n{text_add}"
                file.write(result)
                file.close()
                showwarning(title="Выполнено", message="Результат записан!")
            except:
                showerror(title="Ошибка", message="Что-то пошло не так.")


def start():
    global current_text
    global start_time
    global mistakes
    global stop_test

    stop_test = False
    textbox.config(state="normal")
    window.title("Написано: 0%")

    random_text = random.randint(0, len(variants) - 1)

    start_btn.destroy()
    info_lbl.destroy()

    restart_btn = Button(
        frame,
        text="Перезапустить тест",
        cursor="hand2",
        foreground="#ffff00",
        background="#969600",
        font=("Comic Sans MS", 12),

        command=lambda: start()
    )
    restart_btn.grid(row=4, column=1)

    current_text = variants[random_text]
    mistakes = len(current_text)

    text_lbl.config(text=current_text)
    text_lbl.grid(row=5, column=1, pady=30)

    textbox.grid(row=6, column=1, pady=10)
    textbox.delete("1.0", END)
    textbox.focus_set()

    start_time = time.time()


def time_convert(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    result = f"{int(hours)}:{int(mins)}:{int(sec)}"
    return result


def show():
    file = open('./files/History.txt', 'r', encoding='utf-8')
    messagebox.showinfo('История', file.read())


def clear():
    if askyesno(title="Очистить историю", message="Вы действительно хотите очистить историю?"):
        try:
            open('./files/History.txt', 'w', encoding='utf-8').close()
            showwarning(title="Выполнено", message="История очищена!")
        except:
            showerror(title="Ошибка", message="Что-то пошло не так.")


def category_wpm():
    root = Tk()
    root.withdraw()
    wpm = simpledialog.askstring(title="WPM", prompt="Какой WPM показал наш тест?")
    try:
        wpm = int(wpm)
        if wpm < 30:
            messagebox.showinfo('Результат', "У вас медленный темп печати.")
        elif 30 <= wpm <= 60:
            messagebox.showinfo('Результат', "У вас средний темп печати.")
        elif 60 <= wpm <= 100:
            messagebox.showinfo('Результат', "У вас быстрый темп печати.")
        elif wpm > 100:
            messagebox.showinfo('Результат', "У вас сверхбыстрый темп печати.")
    except:
        showerror(title="Ошибка", message="Что-то пошло не так.")


window = Tk()
window.title("Проверка скорости печати")
window.geometry("750x800")
window.option_add("*tearOff", FALSE)

frame = Frame(
    window,
    padx=10,
    pady=10
)
frame.pack(expand=True)

main_menu = Menu()
history_menu = Menu()
history_menu.add_command(label="Показать", command=show)
history_menu.add_command(label="Очистить", command=clear)
main_menu.add_cascade(label="История", menu=history_menu)
main_menu.add_cascade(label="Узнать темп печати", command=category_wpm)
window.config(menu=main_menu)

header_lbl = Label(
    frame,
    text="Проверка скорости печати",
    font=("Comic Sans MS", 20),
    fg="blue"
)
header_lbl.grid(row=1, column=1, pady=10)

info_lbl = Label(
    frame,
    text="Когда будете готовы, нажмите на кнопку ниже.\nПрограмма выберет случайный текст, "
         "сгенерированный нейросетью. Вам нужно просто написать его без ошибок. "
         "Все ошибки помечаются восклицательными знаками. Допущенные ошибки нужно исправить, иначе тест не завершится. "
         "Тест будет завершён, когда он будет полностью совпадать с оригиналом.",
    font=("Comic Sans MS", 16),
    wraplength=650
)
info_lbl.grid(row=2, column=1, pady=10)

letters_lbl = Label(
    frame,
    text="ВНИМАНИЕ!\nВ тексте всего один абзац.\nСоблюдайте регистр (большие и маленькие буквы - это разные символы),\n"
         "а также буквы 'Е' и 'Ё' - тоже разные символы.",
    font=("Comic Sans MS", 16),
    fg="red",
    wraplength=650
)
letters_lbl.grid(row=3, column=1, pady=10)

start_btn = Button(
    frame,
    text="Начать тест",
    cursor="hand2",
    foreground="#ff0000",
    background="#960000",
    font=("Comic Sans MS", 18),
    width=15,
    command=lambda: start()
)
start_btn.grid(row=4, column=1, pady=30)

text_lbl = Label(
    frame,
    text="Здесь будет текст для теста",
    font=("Comic Sans MS", 18),
    wraplength=700
)

textbox = Text(
    frame,
    width=50,
    height=3,
    font=("Comic Sans MS", 16)
)
textbox.bind("<KeyRelease>", change)

window.mainloop()
