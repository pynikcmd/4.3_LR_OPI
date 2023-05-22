#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
В некой игре-стратегии есть солдаты и герои. У всех есть свойство, содержащее уникальный
номер объекта, и свойство, в котором хранится принадлежность команде. У солдат есть
метод "иду за героем", который в качестве аргумента принимает объект типа "герой". У
героев есть метод увеличения собственного уровня.
В основной ветке программы создается по одному герою для каждой команды. В цикле
генерируются объекты-солдаты. Их принадлежность команде определяется случайно.
Солдаты разных команд добавляются в разные списки.
Измеряется длина списков солдат противоборствующих команд и выводится на экран. У
героя, принадлежащего команде с более длинным списком, увеличивается уровень.
Отправьте одного из солдат первого героя следовать за ним. Выведите на экран
идентификационные номера этих двух юнитов.
"""

import random


class Unit:
    def __init__(self, number, teamid):
        self.number = number
        self.teamid = teamid


class Hero(Unit):
    def __init__(self,  number, teamid, name, level=1):  # При инициализации добавляем свойства name и level
        Unit.__init__(self, number, teamid)
        self.name = name  # Привязываем классу Hero свойство level и name
        self.level = level

    def getlevel(self):
        return self.level

    def inclevel(self):
        self.level += 1
        print('Уровень героя', self.name,'увеличен на 1 и равен', self.level)


class Soldier(Unit):
    def gotohero(self, Hero):
        print('Солдат номер', self.number, 'следует за героем', Hero.name, 'с номером', Hero.number)


def main():
    hero1 = Hero(1, 1, 'One')  # Создаем героев с номерами 1 и 2
    hero2 = Hero(2, 2, 'Two')
    team1, team2 = [], []
    for i in range(2, 12):  # Генерим нечетное количество солдат
        n = random.randint(0, 1)
        if n:
            team1.append(Soldier(i, 1))
            print('Солдат с номером', i, 'добавлен в армию', hero1.name)
        else:
            team2.append(Soldier(i, 2))
            print('Солдат с номером', i, 'добавлен в армию', hero2.name)

    print('Армия героя', hero1.name, ':', len(team1))
    print('Армия героя', hero2.name, ':', len(team2))

    if len(team1) > len(team2):
        print('В армии', hero1.name, 'больше солдат, увеличиваем его уровень')
        hero2.inclevel()
    else:
        print('В армии', hero2.name, 'больше солдат, увеличиваем его уровень')
        hero2.inclevel()

    team1[1].gotohero(hero2)


if __name__ == "__main__":
    main()
