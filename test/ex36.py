# Модули ======================================================================
from sys import exit
# from sys import argv

# script, history = argv

# Функции событий =============================================================
# АКТ 1
def act_1(choice):
    if choice == "1":
        print("Обнажив оружие, Вы нападаете на зверя!")
    elif choice == "2":
        print("Ласково посвистывая, Вы подзываете лису и она, прижимая уши, подкрадывается.")
    elif choice == "3":
        if hero_characteristic[4] >= 4:
            print("\n\t Характеристика [Ловкость] - успех!\n")
            print("Вы спокойно проходите мимо, не провоцируя дикого зверя.")
        else:
            print("Долгое ожидание пугает и раздражает зверя. Он нападает!")
            dead("Лиса Вас загрызла.")
    else:
        print("Долгое ожидание пугает и раздражает зверя. Он нападает!")
        dead("Лиса Вас загрызла.")

# АКТ 2
def act_2(choice):
    if choice == "1":
        print("Обнажив оружие, Вы нападаете на орка!")
    elif choice == "2":
        print("Вы достаете книгу заклинаний и готовитесь наложить чары.")
        if hero_characteristic[2] >= 4:
            print("\n\t Характеристика [Интеллект] - успех!\n")
            magic_book(choice)
        else:
            print("\n\t Характеристика [Интеллект] - провал!\n")
    elif choice == "3":
        if hero_characteristic[4] >= 4:
            print("\n\t Характеристика [Ловкость] - успех!\n")
            print("Вы спокойно проходите мимо, не провоцируя орка.")
        else:
            print("Ваша нерешительность раздражают орка. Он нападает!")
            dead("Орк зарубил Вас.")
    else:
        print("Ваша нерешительность раздражают орка. Он нападает!")
        dead("Орк зарубил Вас.")

# Функции создания персонажа ==================================================
# Проверка на ввод имени героя
def hero_name(name):
    if name == '':
        return hero_name(input("Имя героя: "))
    else:
        return name

# выбор пола персонажа
def hero_sex(who):
    if who == "Мужчина":
        hero_characteristic[0] = 7      # Сила                  - урон в ближнем бою
        hero_characteristic[1] = 4      # Выносливость          - кол-во здоровья и запаса сил
        hero_characteristic[2] = 5      # Интеллект             - урон от магии
        hero_characteristic[3] = 5      # Сила воли             - запас маны
        hero_characteristic[4] = 5      # Ловкость              - шанс уворота
        hero_characteristic[5] = 5      # Скорость              - шанс сбежать
        hero_characteristic[6] = 3      # Привлекательность     - шанс убеждения
        hero_characteristic[7] = 5      # Удача                 - влияет на большинство действий
    elif who == "Женщина":
        hero_characteristic[0] = 3
        hero_characteristic[1] = 6
        hero_characteristic[2] = 5
        hero_characteristic[3] = 5
        hero_characteristic[4] = 5
        hero_characteristic[5] = 5
        hero_characteristic[6] = 7
        hero_characteristic[7] = 5
    else:
        return hero_sex(input("Пол героя [мужчина / женщина]: "))

# выбор класса персонажа
def hero_class(who):
    if who == "Воин":
        hero_characteristic[0] += 2      # Сила
        hero_characteristic[1] += 2      # Выносливость
        hero_characteristic[2] -= 2      # Интеллект
    elif who == "Маг":
        hero_characteristic[0] -= 2      # Сила
        hero_characteristic[1] -= 2      # Выносливость
        hero_characteristic[2] += 3      # Интеллект
        hero_characteristic[3] += 3      # Сила воли
    elif who == "Бард":
        hero_characteristic[0] -= 2      # Сила
        hero_characteristic[1] -= 2      # Выносливость
        hero_characteristic[3] -= 1      # Сила воли
        hero_characteristic[4] += 3      # Ловкость
        hero_characteristic[5] += 4      # Скорость
        hero_characteristic[6] += 2      # Привлекательность
        hero_characteristic[7] += 1      # Удача
    else:
        return hero_class(input("Класс героя: [Воин / Маг / Бард]: "))

# Книга заклинаний
def magic_book(choice):
    spells = {
        'Восстановление': 'Лечение',
        'Разрушение': 'Огненная стрела',
        'Колдовство': 'Призвать дух'
    }

    print(f"""\n Выберите чары:
    1. {spells.get('Восстановление')}
    2. {spells.get('Разрушение')}
    3. {spells.get('Колдовство')}
    """)

    what = input('> ')

    if what == "1":
        print(f"Примененно \'{spells.get('Восстановление')}\' школы \'Восстановление\'")
    elif what == "2":
        print(f"Примененно \'{spells.get('Разрушение')}\' школы \'Разрушение\'")
    elif what == "3":
        print(f"Примененно \'{spells.get('Колдовство')}\' школы \'Колдовство\'")
    else:
        return magic_book(input("Выберите чары: "))

# Создание персонажа ==========================================================
print("\t\n === START GAME === \n")

hero_name = hero_name(input("Имя героя: ")) # Имя
hero_characteristic = [0, 0, 0, 0, 0, 0, 0, 0] # Главные характеристики
hero_sex = hero_sex(input("Пол героя [мужчина / женщина]: ")) # Пол
hero_class = hero_class(input("Класс героя: [Воин / Маг / Бард]: ")) # Класс
health = hero_characteristic[1] * 10 # HP - Здоровье
mana = hero_characteristic[3] * 10 # MP - Мана
stamina = hero_characteristic[1] * 10 # SP - Запас сил

# Смерть героя / врага ========================================================
def dead(why):
    print(why, "Это конец!")
    print("\t\n === YOU DEAD === \n")
    exit(0)

# Старт =======================================================================
def start():
    print(f"""\t\n\n Ваш герой:
===============================
    Имя: {hero_name}       HP: {health}
    Пол: {hero_sex}     MP: {mana}
    Класс: {hero_class}      ST: {stamina}

    Сила:               - {hero_characteristic[0]}
    Выносливость:       - {hero_characteristic[1]}
    Интеллект:          - {hero_characteristic[2]}
    Сила воли:          - {hero_characteristic[3]}
    Ловкость:           - {hero_characteristic[4]}
    Скорость:           - {hero_characteristic[5]}
    Привлекательность:  - {hero_characteristic[6]}
    Удача:              - {hero_characteristic[7]}
===============================
    """)

start()

print("\nИстория начинается!\n\n")



# ================================= ИГРА ======================================
# Событие 1 ===================================================================
print("\t\t\tАКТ I\n\n")

print("""\nПеред Вами на тропинку выскакивает лиса.
На первый взгляд это обычное животное.""")
print("\n Что будете делать?")

print("1. Напасть на лису.")
print("2. Подозвать лису и приласкать её.")
print("3. Пройти мимо, не обращая внимания.")

act_1(input("> "))

# Событие 2 ===================================================================
print("\n\n\t\t\tАКТ II\n\n")

print("\nПеред Вами орк готовый напасть на вас.")
print("\n Что будете делать?")

print("1. Достать меч и сражаться.")
print("2. Наложить чары.")
print("3. Убежать.")

act_2(input("> "))
