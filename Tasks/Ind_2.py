#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Создать абстрактный базовый класс Triad с виртуальными методами
увеличения на 1. Создать производные классы Date (дата) и Time (время).
"""

from abc import ABC, abstractmethod


class Triad(ABC):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @abstractmethod
    def increase(self):
        pass

    @abstractmethod
    def output(self):
        pass


class Date(Triad):
    def __init__(self, day, month, year):
        super().__init__(day, month, year)

    def increase(self):
        self.a += 1  # Увеличение дня на 1
        self.b += 1  # Увеличение месяца на 1
        self.c += 1  # Увеличение года на 1

    def output(self):
        print(f"Дата: {self.a}.{self.b}.{self.c}")


class Time(Triad):
    def __init__(self, hour, minute, second):
        super().__init__(hour, minute, second)

    def increase(self):
        self.a += 1  # Увеличение часа на 1
        self.b += 1  # Увеличение минуты на 1
        self.c += 1  # Увеличение секунды на 1

    def output(self):
        print(f"Время: {self.a}:{self.b}:{self.c}")


def output_triad(triad):
    triad.increase()  # Виртуальный вызов метода increase() для переданного объекта
    triad.output()  # Вызов переопределенного метода output() для переданного объекта


if __name__ == '__main__':
    # Создание объектов класса Date и класса Time
    date = Date(12, 5, 2022)
    time = Time(10, 30, 45)

    output_triad(date)  # Вывод и увеличение даты
    output_triad(time)  # Вывод и увеличение времени

