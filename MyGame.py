# Главные характеристики
class Characteristic(object):

    # базовые значения
    dic_char = {
        'Сила': 5,                    # урон в ближнем бою
        'Выносливость': 5,            # кол-во здоровья и запаса сил
        'Интеллект': 5,               # урон от магии
        'Сила воли': 5,               # запас маны
        'Ловкость': 5,                # шанс уворота
        'Скорость': 5,                # шанс сбежать
        'Привлекательность': 5,       # шанс убеждения
        'Удача': 5                    # влияет на большинство действий
    }


# Создание персонажа
class Character_Creation(Characteristic):

    # Ввод имени героя и проверка на ввод
    def hero_name(self):

        name = input("Имя героя: ")

        if name == '':
            return my_hero.hero_name()
        else:
            return name

    # Выбор пола персонажа и проверка на ввод
    def hero_sex(self):

        sex = input("Пол героя [Мужчина / Женщина]: ")

        if sex == "Мужчина":
            my_hero.dic_char['Сила'] += 2
            my_hero.dic_char['Выносливость'] -= 1
            my_hero.dic_char['Привлекательность'] -=2
            return sex
        elif sex == "Женщина":
            my_hero.dic_char['Сила'] -= 2
            my_hero.dic_char['Выносливость'] += 1
            my_hero.dic_char['Привлекательность'] += 2
            return sex
        else:
            return my_hero.hero_sex()

    # Выбор класса персонажа и проверка на ввод
    def hero_class(self):

        who = input("Класс героя: [Воин / Маг / Бард]: ")

        if who == "Воин":
            my_hero.dic_char['Сила'] += 2
            my_hero.dic_char['Выносливость'] += 2
            my_hero.dic_char['Интеллект'] -= 2
            return who
        elif who == "Маг":
            my_hero.dic_char['Сила'] -= 2
            my_hero.dic_char['Выносливость'] -= 2
            my_hero.dic_char['Интеллект'] += 3
            my_hero.dic_char['Сила воли'] += 3
            return who
        elif who == "Бард":
            my_hero.dic_char['Сила'] -= 2
            my_hero.dic_char['Выносливость'] -= 2
            my_hero.dic_char['Сила воли'] -= 1
            my_hero.dic_char['Ловкость'] += 3
            my_hero.dic_char['Скорость'] += 4
            my_hero.dic_char['Привлекательность'] += 2
            my_hero.dic_char['Удача'] += 1
            return who
        else:
            return my_hero.hero_class()

my_hero = Character_Creation() # создается объекм Мой Герой


# Пересоздать персонажа или начать игру
#class Engine(object):

    # начать игру
#    def play(self):
#        pass

    # пересоздать персонажа
#    def new_character(self):
#        pass


# Вывод параметров героя
print(f"""\n\n\tВаш герой:
===============================
 Имя: {my_hero.hero_name()}
 Пол: {my_hero.hero_sex()}
 Класс: {my_hero.hero_class()}

 HP: {my_hero.dic_char['Сила'] * 10}
 MP: {my_hero.dic_char['Интеллект'] * 10}
 ST: {my_hero.dic_char['Выносливость'] * 10}

 Сила:               - {my_hero.dic_char['Сила']}
 Выносливость:       - {my_hero.dic_char['Выносливость']}
 Интеллект:          - {my_hero.dic_char['Интеллект']}
 Сила воли:          - {my_hero.dic_char['Сила воли']}
 Ловкость:           - {my_hero.dic_char['Ловкость']}
 Скорость:           - {my_hero.dic_char['Скорость']}
 Привлекательность:  - {my_hero.dic_char['Привлекательность']}
 Удача:              - {my_hero.dic_char['Удача']}
===============================
    """)


class Choice(object):

    def sarcophagus(self, choice):
        if choice == '1':
            print('\n [Выбрано действие первое]')
            return choice
        elif choice == '2':
            print('\n [Выбрано действие второе]')
            return choice
        elif choice == '3':
            print('\n [Выбрано действие третье]')
            return choice
        else:
            pass

    def skeleton(self, choice):
        if choice == '1':
            print('\n [Выбрано действие первое]')
            return choice
        elif choice == '2':
            print('\n [Выбрано действие второе]')
            return choice
        else:
            pass

    def puzzle(self, choice):
        if choice == '1':
            print('\n [Выбрано действие первое]')
            return choice
        elif choice == '2':
            print('\n [Выбрано действие второе]')
            return choice
        else:
            pass

choice = Choice() # создается объект Выбор


# События
class Events(Choice):

    # Саркофаг
    def sarcophagus(self):

        print("""
            "Саркофаг" - герой находит запертый саркофаг, который обязательно нужно открыть.
            Есть три варианта решения задачи: взломать (требует отмычку - есть у барда),
            отпереть силой, (если специальность Воин), прочитать руны (если Маг).
            Когда саркофаг будет открыт, игрок получит свиток с загадкой, которую не сможет прочитать.
            Свиток понадобится в конце.
        """)
        print("\n Что будете делать?\n")

        print("1. Действие первое.")
        print("2. Действие второе.")
        print("3. Действие третье.")

        choice.sarcophagus(input('\n\t > '))

    # Скелет
    def skeleton(self):
        print("""
            "Скелет" - герой встречает врага-скелета, которого необходимо победить.
        """)
        print("\n Что будете делать?")

        print("1. Действие первое.")
        print("2. Действие второе.")

        choice.skeleton(input('\n\t > '))

    # Загадка
    def puzzle(self):
        print("""
            "Загадка" - герой находит говорящую дверь с лицом, которая может прочитать свиток с загадкой.
            Игрок сам вводит ответ, если он правильный, герой проходит в дверь-портал и попадает во второй акт,
            иначе - пробует снова отгадать.
        """)
        print(" Что будете делать?")

        print("1. Действие первое.")
        print("2. Действие второе.")

        choice.puzzle(input('\n\t > '))

events = Events() # создается объект События


# Сцены
class Scene(Character_Creation):

    # Смерть
    def dead(why):
        print(why, "Это конец!")
        print("\t\n === YOU DEAD === \n")
        exit(0)

    # АКТ 1
    def act_1(self):
        events.sarcophagus() # запускаем сцену "Саркофаг"
        events.skeleton() # запускаем сцену "Скелет"
        events.puzzle() # запускаем сцену "Загадка"

scene = Scene() # создается объект Сцен


scene.act_1() # запускаем Акт 1
