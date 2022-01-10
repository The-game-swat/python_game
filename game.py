import os
import random
from random import randint
import time

typingsleep = randint(1, 2)

print("\n\nПривет:) Добро пожаловать в игру The_Game_SWAT")

time.sleep(typingsleep)

# Привесвие пользователя и основное меню игры
while True:
    print("""\n
    Введите start - чтобы начать игру.
    Введите help - для вывода справки.
    Введите exit - для выхода
    """)
    command = input(">")
    if command == "start":
        break
    elif command == "help":
        print("""Игора The_Game_swat
        Игра призвана тренировать интуицию, и поможет проверить твою удачливость!
        В неравном бою между человек и машиной тебе прийдется не сладко!
        Правила игры:
        1. Игра на подобе бесцеллера "21 очко";
        2. Нужно набрать количество очков как можно ближе к 21, НО не более иначе соперник победит.
        3. И только для тебя, нежданчик, за каждый ход, ты будешь терять здоровье, но и за каждую победу будешь оздоравливаться!
        Дерзай:Ъ
        """)
    elif command == "exit":
        exit()
    else:
        print("")

# Конфиг игры, стратовые значения и ограничения
count = 0
count_comp = 0
healer_user = 0
healer_comp = 0
health_user = 100
health_comp = 100

# Основной цикл игры, в котором происходят взаимоействие с пользователем
while True:
    koloda = [6, 7, 8, 9, 10, 2, 3, 4, 11]
    lite_hit = random.randrange(18, 25)
    middle_hit = random.randrange(10, 35)
    random.shuffle(koloda)

    choice = input('\nВзять карту? y/n: >')
    if choice == 'y':
        current = koloda.pop()
        current_comp = koloda.pop()
        count += current
        count_comp += current_comp
        health_user -= lite_hit
        health_comp -= middle_hit
        print('Вам выпало %s очков' % current +
              '. И нанесен урон %d' % lite_hit)

    if count > 21:
        print('Соперник победил!')
        print(health_comp)
        break

    elif count == 21:
        print('Поздравляю, вы победили!')
        break

    elif count_comp > 21:
        print('Поздравляю, вы победили!')
        break
    elif count_comp == 21:
        print('Соперник победил!')
        print(health_comp)
        break

    else:
        print('Всего: %d очков.' % count +
              ' И %s здоровье' % health_user + '\n' +
              ' =' * 20)
        time.sleep(typingsleep)
        print('Ход соперника! Соперник походил!')
        print(' =' * 20)
        time.sleep(typingsleep)

    if choice == 'n':
        if count > count_comp:
            h = random.randint(18, 25)
            a = h + health_user
            print('Вы победили! УРА! Получаешь + %s к здоровью' % h)
            time.sleep(typingsleep)
            print('У вас - %d очков. ' % count + ' Здоровье - %s' % a)
            ' - ' * 20
            print('У соперника - %d очков.' % count_comp + ' Здоровье - %s' % health_comp)
        else:
            if count_comp > count:
                h = random.randint(18, 25)
                a = h + health_user
                print('Сорян, БРО! Ты проиграл \nСоперник получает + %s к здоровью' % h)
                time.sleep(typingsleep)
                print('У вас - %d очков. ' % count + ' Здоровье - %s' % a)
                ' - ' * 20
                print('У соперника - %d очков.' % count_comp + ' Здоровье - %s' % health_comp)
                break
            else:
                h = random.randint(18, 25)
                a = h + healer_comp
                print('Вы победили! УРА! Получаешь + %s к здоровью' % h)
                time.sleep(typingsleep)
                print('У вас - %d очков.' % count + ' Здоровье - %s' % a)
                ' - ' * 20
                print('У соперника - %d очков.' % count_comp + 'Здоровье - %s' % health_comp)
                break
        break
print('#' * 20)
print('Спасибо за игру!')
print('#' * 20)
